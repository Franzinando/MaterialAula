from machine import Pin, ADC, PWM
from time import sleep
import math

pot = ADC(Pin(32))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT) #seta 12 bits(faixa de 0 - 4095)

led = PWM(Pin(23), freq = 20000, duty = 0)

def map(leitura):
    tensao = leitura * (3.3 / 4095)
    tensao = int(tensao * 310) #Tensão máxima(3.3)
    # 3.3 * 310 == 1023
    return tensao

while True:
    duty = map(pot.read())
    print(pot.read(), duty)
    led.duty(duty)
    sleep(0.2)