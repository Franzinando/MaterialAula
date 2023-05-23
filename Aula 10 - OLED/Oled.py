from time import sleep
from machine import Pin, I2C, TouchPad
import ssd1306

i2c = I2C(scl=Pin(21), sda=Pin(23))
led = Pin(2, Pin.OUT)
oled_width = 128 #Largura
oled_height = 64 #Altura
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

leitura = TouchPad(Pin(4))

i=0
oled.contrast(255)
oled.fill(0)
oled.text('  FATEC JUNDIAI', 0, 0)
oled.text('    OFICINA', 0, 25)
oled.text('  FRANZINANDO', 0, 40)
oled.text('    AULA 10', 0, 55)
oled.show()
sleep(3)
oled.fill(0)

while True:
    capacitivo = leitura.read()
    i+=1
    oled.fill(0) #Limpa o Display
    oled.contrast(255)
    oled.text('  TESTE DISPLAY', 0, 0)
    oled.text('Sensor', 0, 20)
    oled.text('Capacitivo', 0, 35)
    oled.text('>>> '+str(capacitivo), 0, 50)
    oled.show() #exibir as informações
    if capacitivo<=300:
        led.value(1)
    else:
        led.value(0)
    sleep(1)