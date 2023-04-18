from machine import Pin, PWM, ADC
from time import sleep
import math

def converter(x, in_min,in_max,out_min,out_max):
    conta = math.trunc((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    return conta

def angulo(x):
    angulo = converter(x, 0,4095,20,120)
    print('angle',angulo)
    servo.duty(angulo)

servo = PWM(Pin(23), freq = 50) #frequência de servomecanismo

pot = ADC(Pin(32))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT) #seta 12 bits(faixa de 0 - 4095)

while True:
    angle = pot.read()
    print(pot.read())
    angulo(angle)
    sleep(0.1)