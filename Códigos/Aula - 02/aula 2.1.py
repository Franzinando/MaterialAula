from machine import Pin #acessar os pinos da placa
from time import sleep#intervalos de temporização
#import time

led = Pin(23, Pin.OUT) #Configurar o pino 2 como uma saída digital

while True:
    led.value(1) #liga o led
    sleep(1) #aguarda 1 segundo
    led.value(0) #desliga o led
    sleep(1)