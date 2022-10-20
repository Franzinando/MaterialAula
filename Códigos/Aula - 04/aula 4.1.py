#Aula 4 - PWM

from machine import Pin, ADC, PWM
from time import sleep

led = PWM(Pin(23))

while True:
    #for --> estrutura de repetição
    #range --> intervalo de valores com icremento
    
    for i in range(0, 1023, 5):
        led.duty(i)  #enviar o valor para o LED
        sleep(0.05)
        
    for i in range(1023,0, -5):
        led.duty(i)  #enviar o valor para o LED
        sleep(0.05)