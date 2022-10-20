import network
import usocket as socket
import gc
import machine 
gc.collect()

html = """<!DOCTYPE html>
<html>
    <head>
        <title>NodeMCU LED</title>
        <meta charset="utf-8">
    </head>
    <body>
        <form>
            <h1>LED:</h1>
            <p align="center">
                #Adicionando dois botões a página HTML
                <button name="LED" value="ON" type="submit">Ligar</button>&nbsp;&nbsp;
                <button name="LED" value="OFF" type="submit">Desligar</button><br>
            </p>
        </form>
    </body>
</html>
"""

LED = machine.Pin(23, machine.Pin.OUT)

estacao = network.WLAN(network.STA_IF)
estacao.active(True)
estacao.connect('Ventura','1145823242am')

while estacao.isconnected()==False:
    pass
print('Conexão Realizada')
print(estacao.ifconfig())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

try:
    while True:
        conexao, endereco = s.accept()
        print('Conexão de %s' %str(endereco))
        requisicao = conexao.recv(1024)
        requisicao = str(requisicao)
        print('Conteudo = %s' % requisicao)
        
        #Identificar a requisição enviada ao servidor, ou seja,
        #qual botão foi apertado.
        
        if requisicao.find('GET /?LED=ON') != -1:
            LED.value(1)
        if requisicao.find('GET /?LED=OFF') != -1:
            LED.value(0)
            
        conexao.send('HTTP/1.1 200 OK\n')
        conexao.send('Content-Type: text/html\n')
        conexao.send('Connection: close\n\n')
        conexao.sendall(html)
        conexao.close
        
except KeyboardInterrupt:
    s.close()
    estacao.active(True)