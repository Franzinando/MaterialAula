#Aula 3 - Sinal Analóico

from machine import Pin, ADC
from time import sleep

ldr = ADC (Pin(32))
ldr.atten(ADC.ATTN_11DB)

while True:
    ldr_leitura = ldr.read()
    print(ldr_leitura)
    sleep(2)
