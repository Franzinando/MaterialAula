#Aula 3 - Sinal Analógico

from machine import Pin, ADC
from time import sleep

led = Pin(21, Pin.OUT) 

led2 = Pin(22, Pin.OUT)  

led3 = Pin(23, Pin.OUT) 

ldr = ADC(Pin(32))  #configurar o pino com entrada analógica
ldr.atten(ADC.ATTN_11DB)

min = 0
max = 4095

while True:
    ldr_leitura = ldr.read() #associar o valor recebido a variável a ldr_leitura
    
    if ldr_leitura>=min and ldr_leitura<=(max/3):
        led.value(1)
        led2.value(1)
        led3.value(1)
        
    elif ldr_leitura>(max/3) and ldr_leitura<=(max/2):
        led.value(1)
        led2.value(1)
        led3.value(0)
        
    elif ldr_leitura>(max/2) and ldr_leitura<=(max):
        led.value(1)
        led2.value(0)
        led3.value(0)
        
    print(ldr_leitura)
    sleep(1)