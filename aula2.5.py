#Aula 2: Sinal Digital

import board            
from time import sleep  
from digitalio import DigitalInOut, Direction 

vermelho = DigitalInOut(board.IO3)                               
vermelho.direction = Direction.OUTPUT

amarelo = DigitalInOut(board.IO4)                               
amarelo.direction = Direction.OUTPUT

verde = DigitalInOut(board.IO5)                               
verde.direction = Direction.OUTPUT

vermelho_pedestre = DigitalInOut(board.IO7)                               
vermelho_pedestre.direction = Direction.OUTPUT

verde_pedestre = DigitalInOut(board.IO6)                               
verde_pedestre.direction = Direction.OUTPUT

botao = DigitalInOut(board.IO2)   # mapea para pino 3
botao.direction = Direction.INPUT # configura como entrada

estado = 0

while True:
    #carro
    vermelho.value=0
    amarelo.value=0
    verde.value= 1
    #pedestre
    vermelho_pedestre.value=1
    verde_pedestre.value=0
    
    if botao.value==1:
        
        verde.value= 0
        
        amarelo.value=1
        sleep(0.5)
        amarelo.value=0
        sleep(0.5)
        amarelo.value=1
        sleep(0.5)
        
        amarelo.value=0
        vermelho_pedestre.value=0
        sleep(0.5)
        
        verde_pedestre.value =1
        vermelho.value=1
        sleep(5)
        
        
        