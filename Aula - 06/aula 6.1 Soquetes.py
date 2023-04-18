import network
import usocket as socket
import gc
gc.collect()

#Variável que contém a página HTML que será
#enviada para o servidor.
html = """<!DOCTYPE html>
<html>
    <head>
        <title>Olá</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Olá!</h1>
    </body>
</html>
"""

#Conexão a um access point
estacao = network.WLAN(network.STA_IF)
estacao.active(True)
estacao.connect('ap','senha')

while estacao.isconnected()==False:
    pass
print('Conexão Realizada')
print(estacao.ifconfig())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Criação de um soquete
s.bind(('', 80)) #Ligação do soquete a uma porta TCP 80(porta padrão usada pelo protocolo HTML)
s.listen(5) #máximo de solicitações de conexões simultâneas

try:
    while True: #laço que aceit PEDIDOS de conexão, PROCESSA a requisição do cliente e
                #ENVIA o contéudo
        conexao, endereco = s.accept()
        print('Conexão de %s' %str(endereco))
        requisicao = conexao.recv(1024)
        requisicao = str(requisicao)
        print('Conteudo = %s' % requisicao)
        
        #Envio do cabeçalho
        conexao.send('HTTP/1.1 200 OK\n')
        conexao.send('Content-Type: text/html\n')
        conexao.send('Connection: close\n\n')
        conexao.sendall(html) #Instruções HTML
        conexao.close()#Encerra a conexão com o cliente
except KeyboardInterrupt:
    s.close()
    estacao.active(True)