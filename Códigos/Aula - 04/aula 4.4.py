from machine import Pin, PWM
from time import sleep
import math

red = PWM(Pin(21))
green = PWM(Pin(22))
blue = PWM(Pin(23))

def converter(x, comum):
    if comum.lower() == 'catodo':
        in_min=0
        in_max=255
        out_min=0
        out_max=1023
    elif comum.lower() == 'anodo':
        in_min=0
        in_max=255
        out_min=1023
        out_max=0
    conta = math.trunc((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    return conta

def rgb(r, g, b):
    red.duty(converter(r, 'anodo'))
    green.duty(converter(g, 'anodo'))
    blue.duty(converter(b, 'anodo'))  

while True:
    #para i que inicia em em zero e termina em 255
    #em um intervalo de 1
    for i in range(0, 255, 1):  #Inicia no verde
        rgb(0, 255 - i, i)
        sleep(0.05)
        
    for i in range(255, 0, -1):
        rgb(255-i, 0, i)
        sleep(0.05)
        
    for i in range(255, 0, -1):
        rgb(i, 255-i, 0)
        sleep(0.05)