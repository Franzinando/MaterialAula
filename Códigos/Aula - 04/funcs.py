import math

def map(x, in_min, in_max, out_min, out_max):
    conta = math.trunc((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    return conta

def map(x, comum):
    if comum.upper == 'C':
        in_min=0
        in_max=255
        out_min=0
        out_max=1023
    elif comum.upper == 'A':
        in_min=255
        in_max=0
        out_min=1023
        out_max=0
    else:
        print('Erro!')
    conta = math.trunc((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    return conta

def catodo(x):
    conta = math.trunc((x - 0) * (1023 - 0) / (255 - 0) + 0)
    return conta

def anodo(x, in_min, in_max, out_min, out_max):
    conta = math.trunc((x - 255) * (0 - 1023) / (0 - 255) + 1023)
    return conta

def rgb(red, gree,blue):
    red.duty(map2(255))
    green.duty(map2(255))
    blue.duty(map2(0))

print(map(255, 0, 255, 0, 1023), map2(255))

