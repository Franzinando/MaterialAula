#Aula 2: Sinal Digital

#Módulos Necessários
import board #acessar os pinos da placa
from time import sleep #intervalos de temporização
#import time
from digitalio import DigitalInOut, Direction #setup dos pinos digitais

#Configurando o pino como saída digital
led = DigitalInOut(board.IO2) #Associar o pino 2 da placa a variável led
                              #e identificá-lo como um pino digital
led.direction = Direction.OUTPUT #declarar esse pino como uma saída digital

while True: #laço de repetição infinito (loop)
    led.value = 1 #liga o led
    sleep(1) #aguarda 1 segundo
    led.value = 0 #desliga o led
    sleep(1)
