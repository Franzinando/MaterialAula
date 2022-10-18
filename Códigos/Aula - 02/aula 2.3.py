#Aula 2: Sinal Digital

#Módulos Necessários
from machine import Pin #acessar os pinos da placa
from time import sleep  #intervalos de temporização

#Configurando o pino como saída digital
led = Pin(2, Pin.OUT)    #Associar o pino 2 da placa a variável led
                         #e identificá-lo como um pino digital

#Configurando o pino como entrada digital
botao = Pin(4, Pin.IN) #mapea para pino 3 e configura como entrada

estado = 0
while True: #laço de repetição infinito (loop)
    
    if botao.value() == 1: #se o botão estiver presionado
        led.value(1)
        sleep(0.2)
        led.value(0)
        sleep(0.2)
    
    else:
        led.value(0)