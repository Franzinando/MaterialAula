#Aula 7 - Controle de Dispositivos pela Internet

import network
import usocket as socket
import machine
import gc
gc.collect()

LED = machine.Pin(23, machine.Pin.OUT)

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

try:
  while True:
    conexao, endereco = s.accept()
    print('Conexao de %s' % str(endereco))
    requisicao = conexao.recv(1024)
    requisicao = str(requisicao)
    print('Conteudo = %s' % requisicao)
    
    if requisicao.find('/led/1') != -1:
      print('Acender')
      LED.value(1)
    elif requisicao.find('/led/0') != -1:
      print('Apagar')
      LED.value(0)
    else:
      LED.value(0)
      
    html = obter_arquivo('http-led-bootstrap.html')
    conexao.send('HTTP/1.1 200 OK\n')
    conexao.send('Content-Type: text/html\n')
    conexao.send('Connection: close\n\n')
    conexao.sendall(html)
    conexao.close()
except KeyboardInterrupt:
  s.close()
  estacao.active(False)