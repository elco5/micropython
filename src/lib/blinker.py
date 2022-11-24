from machine import Pin
from machine import Timer

BLINKER_PIN = 32
blinker = Pin(BLINKER_PIN, Pin.OUT)
tim1 = Timer(1)
tim2 = Timer(2)
tim3 = Timer(3)


tim1 = tim1.init(period=5000, mode=Timer.PERIODIC,
     callback=lambda t:print("Welcome to Microcontrollerslab"))


def blinker_off(t):
    blinker.value(0)
    print('blinker off')

def blinker_on(t):
    blinker.value(1)
    tim3.init(period=100, mode=Timer.ONE_SHOT, callback=blinker_off)
    print('blinker on')

def blinker_start():
    tim2.init(period=1000, mode=Timer.PERIODIC, callback=blinker_on)
    print('blinker started')

blinker_start()