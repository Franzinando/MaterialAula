#Aula 2: Sinal Digital

#Módulos Necessários
import board            #acessar os pinos da placa
from time import sleep  #intervalos de temporização
#import time
from digitalio import DigitalInOut, Direction #setup dos pinos digitais

#Configurando o pino como saída digital
led = DigitalInOut(board.IO2)    #Associar o pino 2 da placa a variável led
                                 #e identificá-lo como um pino digital
led.direction = Direction.OUTPUT # configura como  saída digital

#Configurando o pino como entrada digital
botao = DigitalInOut(board.IO3)   # mapea para pino 3
botao.direction = Direction.INPUT # configura como entrada

estado = 0

while True: #laço de repetição infinito (loop)
    
    if botao.value:           #Se houver alteração no valor do botão,
                              #ou seja, se o botão for pressionado
        estado = not estado   #troca o estado
        
    led.value = estado        #led se comporta de acordo com a variável estado
    print(estado)
    sleep(1)
    