# https://www.mfitzp.com/using-micropython-raspberry-pico/
from machine import Pin, PWM
from time import sleep

led = PWM(Pin(25))

def ledon(brightness=65535):
    led.duty_u16(brightness)


while True:
    for a in range(0, 65536, 10000):
        ledon(a)
        sleep(0.1)