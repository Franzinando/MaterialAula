#Aula 8 - Enviando dados pela WEB

import network
import usocket as socket
from machine import ADC, Pin
import gc
gc.collect()

adc = ADC(Pin(32))
adc.atten(ADC.ATTN_11DB)

def obter_arquivo(arquivo):
    conteudo = ''
    a = open(arquivo, 'rb')
    conteudo = a.read()
    a.close()
    return conteudo

estacao = network.WLAN(network.STA_IF)
estacao.active(True)
estacao.connect('Ventura', '1145823242am')

while estacao.isconnected() == False:
    pass

print('Conexao realizada.')
print(estacao.ifconfig())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

try:
    while True:
        conexao, endereco = s.accept()
        print('Conexao de %s' % str(endereco))
        requisicao = conexao.recv(1024)
        requisicao = str(requisicao)
        
        if requisicao.find('obter/luminosidade') != -1:
            lum = adc.read()
            html = str(round(lum, 1))
        elif requisicao.find('/luminosidade.png') != -1:
            html = obter_arquivo('luminosidade.png')
        elif requisicao.find('/') != -1:
            html = obter_arquivo('http-ldr.html')
        
        conexao.send('HTTP/1.1 200 OK\n')
        conexao.send('Content-Type: text/html\n')
        conexao.send('Connection: close\n\n')
        conexao.sendall(html)
        conexao.close()
        
except KeyboardInterrupt:
    s.close()
    estacao.active(False)