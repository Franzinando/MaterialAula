from machine import Pin, PWM
from time import sleep
import math

def converter(x, in_min,in_max,out_min,out_max):
    conta = math.trunc((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    return conta

def angulo(x):
    angulo = converter(x, 0,180,20,120)
    servo.duty(angulo)

servo = PWM(Pin(23), freq = 50) #frequência de servomecanismo

while True:
    angulo(0) 
    sleep(2)
    angulo(45) 
    sleep(2)
    angulo(90)
    sleep(2)
    angulo(135) 
    sleep(2)
    angulo(180) 
    sleep(2)
    