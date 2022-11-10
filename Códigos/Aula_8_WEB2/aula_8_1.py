#Aula 8 - Enviando dados pela WEB

import network
import usocket as socket
from machine import ADC, Pin
import math
import gc
gc.collect()

adc = ADC(Pin(32))
adc.atten(ADC.ATTN_11DB)

def obter_temperatura(termistor):
    fator = 4096
    TempK = math.log(10000.0*(fator / termistor - 1))
    TempK = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * TempK * TempK))* TempK)
    TempC = TempK - 273.15  #Convert Kelvin to Celsius
    return TempC

def obter_arquivo(arquivo):
    conteudo = ''
    a = open(arquivo, 'rb')
    conteudo = a.read()
    a.close()
    return conteudo

estacao = network.WLAN(network.STA_IF)
estacao.active(True)
estacao.connect('ap', 'senha')

while estacao.isconnected() == False:
    pass

print('Conexao realizada.')
print(estacao.ifconfig())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

html = 0
try:
    while True:
        conexao, endereco = s.accept()
        print('Conexao de %s' % str(endereco))
        requisicao = conexao.recv(1024)
        requisicao = str(requisicao)
        
        if requisicao.find('obter/temperatura') != -1:
            temperatura = obter_temperatura(adc.read())
            print(obter_temperatura(adc.read()))
            print(adc.read())
            html = str(round(temperatura, 1))
        elif requisicao.find('/termometro.png') != -1:
            html = obter_arquivo('termometro.png')
        elif requisicao.find('/') != -1:
            html = obter_arquivo('http-termistor.html')
        
        conexao.send('HTTP/1.1 200 OK\n')
        conexao.send('Content-Type: text/html\n')
        conexao.send('Connection: close\n\n')
        conexao.sendall(html)
        conexao.close()
        
except KeyboardInterrupt:
    s.close()
    estacao.active(False)