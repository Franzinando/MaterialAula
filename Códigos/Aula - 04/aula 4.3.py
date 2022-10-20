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
    #Vermelho
    rgb(255, 0, 0)
    sleep(3)
    #Verde
    rgb(0, 255, 0)
    sleep(3)
    #Azul
    rgb(0, 0, 255)
    sleep(3)
    #Amarelo
    rgb(255, 255, 0)
    sleep(3)
    #Rosa
    rgb(255, 20, 147)
    sleep(3)
    #Azul Claro
    rgb(173,216,230)
    sleep(3)
    rgb(0,0,0)
    
    
    
   