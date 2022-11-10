#Aula 7 - Controle de Dispositivos pela Internet

import network
import usocket as socket
import machine
import math
import gc
gc.collect()

servo = machine.PWM(machine.Pin(23), freq = 50) 

def converter(x, in_min,in_max,out_min,out_max):
    conta = math.trunc((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    return conta

def angulo(x):
    angulo = converter(x, 0,180,20,120)
    servo.duty(angulo)

def obter_arquivo(arquivo):
  conteudo = ''
  a = open(arquivo, 'rb')
  conteudo = a.read()
  a.close()
  return conteudo

estacao = network.WLAN(network.STA_IF)
estacao.active(True)
estacao.connect('ID', 'SENHA')
while estacao.isconnected() == False:
  pass
print('Conexao realizada.')
print(estacao.ifconfig())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

angulo(0)

try:
  while True:
    conexao, endereco = s.accept()
    print('Conexao de %s' % str(endereco))
    requisicao = conexao.recv(1024)
    requisicao = str(requisicao)
    print('Conteudo = %s' % requisicao)
    
    if requisicao.find('/servo/1') != -1:
      print('Abrir')
      angulo(90)
    elif requisicao.find('/servo/0') != -1:
      print('Fechar')
      angulo(0)
    else:
      angulo(0)
      
    html = obter_arquivo('http-servo-bootstrap.html')
    conexao.send('HTTP/1.1 200 OK\n')
    conexao.send('Content-Type: text/html\n')
    conexao.send('Connection: close\n\n')
    conexao.sendall(html)
    conexao.close()
except KeyboardInterrupt:
  s.close()
  estacao.active(False)