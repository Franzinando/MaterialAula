#Aula 3 - Sinal Analógico

from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(32))
buzzer = Pin(21, Pin.OUT)

min = 0
max = 4095

while True:
    pot_leitura = pot.read() #associar o valor recebido a variável a ldr_leitura
    
    if pot_leitura>=min and pot_leitura<=(max/2):
        buzzer.value(0)
    else:
        buzzer.value(1)
        
    print(pot_leitura)
    sleep(2)