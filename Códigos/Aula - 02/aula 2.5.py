#Aula 2: Sinal Digital

from machine import Pin 
from time import sleep 

vermelho = Pin(23, Pin.OUT)
amarelo = Pin(22, Pin.OUT)
verde = Pin(2, Pin.OUT)

vermelho_pedestre = Pin(19, Pin.OUT)
verde_pedestre = Pin(21, Pin.OUT)

botao = Pin(4, Pin.IN)

estado = 0

while True:
    #carro
    vermelho.value(0)
    amarelo.value(0)
    verde.value(1)
    #pedestre
    vermelho_pedestre.value(1)
    verde_pedestre.value(0)
    
    if botao.value()==1:
        
        verde.value(0)
        
        amarelo.value(1)
        sleep(0.5)
        amarelo.value(0)
        sleep(0.5)
        amarelo.value(1)
        sleep(0.5)
        
        amarelo.value(0)
        vermelho_pedestre.value(0)
        sleep(0.5)
        
        verde_pedestre.value(1)
        vermelho.value(1)
        sleep(5)