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

while True:
    
    amarelo.value = 0
    vermelho.value = 0
    verde.value = 1
    sleep(5)
    
    verde.value = 0
    amarelo.value = 1
    sleep(2)
    
    amarelo.value = 0
    vermelho.value = 1
    sleep(5)
   
        