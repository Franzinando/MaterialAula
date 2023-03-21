#Aula 3 - Sinal Analógico

from machine import Pin, ADC
from time import sleep

ldr = ADC(Pin(32))
ldr.atten(ADC.ATTN_11DB)

while True:
    ldr_leitura = ldr.read() #associar o valor recebido a variável a ldr_leitura
    print(ldr_leitura)       #imprimir valor monitor
    sleep(2)    