#Aula 2: Sinal Digital

#Módulos Necessários
from machine import Pin           #acessar os pinos da placa
from time import sleep  #intervalos de temporização

#Configurando o pino como saída digital
led = Pin(2, Pin.OUT)    #Associar o pino 2 da placa a variável led
                                 #e identificá-lo como um pino digital

#Configurando o pino como entrada digital
botao = Pin(4, Pin.IN) #mapea para pino 3 e configura como entrada

estado = 0

while True: #laço de repetição infinito (loop)
    
    if botao.value():           #Se houver alteração no valor do botão,
                              #ou seja, se o botão for pressionado
        estado = not estado   #troca o estado
        
    led.value(estado)        #led se comporta de acordo com a variável estado
    print(estado)
    sleep(1)