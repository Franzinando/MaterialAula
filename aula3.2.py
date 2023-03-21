#Aula 3 - Sinal Analógico

from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(32))
buzzer = Pin(21, Pin.OUT)

while True:
    pot_leitura = pot.read() #associar o valor recebido a variável a ldr_leitura
    print(pot_leitura)       #imprimir valor monitor
    sleep(2)   