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

    O script vai iniciar o processo automaticamente e pedirá que você forneça as informações necessárias, como a porta (LPORT).

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou correções. Caso encontre problemas, por favor, abra uma issue no repositório.
