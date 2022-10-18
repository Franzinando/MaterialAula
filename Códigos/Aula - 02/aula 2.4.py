#Aula 2: Sinal Digital

from machine import Pin 
from time import sleep 

vermelho = Pin(23, Pin.OUT)
amarelo = Pin(22, Pin.OUT)
verde = Pin(2, Pin.OUT)

while True:
    
    amarelo.value(0)
    vermelho.value(0)
    verde.value(1)
    sleep(5)
    
    verde.value(0)
    amarelo.value(1)
    sleep(2)
    
    amarelo.value(0)
    vermelho.value(1)
    sleep(5)