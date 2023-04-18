#Exemplo Thermistor (sem biblioteca)

import math 
from machine import Pin, ADC
from time import sleep

thermistor = ADC(Pin(32))
thermistor.atten(ADC.ATTN_11DB) #Atenuação --> 

def temperature(r):
    fator = 4096
    TempK = math.log(10000.0*(fator / r - 1))
    TempK = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * TempK * TempK))* TempK)
    TempC = TempK - 273.15  #Convert Kelvin to Celsius
    return TempC

while True:
    adc = thermistor.read()
    temperatura = temperature(adc)
    print(temperatura,'°C',adc)
    sleep(1)