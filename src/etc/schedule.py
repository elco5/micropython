# https://docs.micropython.org/en/latest/reference/isr_rules.html?highlight=timer%20callback

print('importing schedule...')
from machine import Timer
import micropython
import time
from machine import Pin
led = Pin(32, Pin.OUT)




def cb1(arg):  # Scheduled callback
    print(arg, 'cb1')
    led.on()

def cb2(arg):  # Scheduled callback
    print(arg, 'cb2')
    led.off()

def cb1_irq(tim):  # Hard IRQ
    micropython.schedule(cb1, 'Timer 1')

def cb2_irq(tim):
    micropython.schedule(cb2, 'Timer 2')




t1 = Timer(1)
t2 = Timer(2)

t1.init(period=1000, mode=Timer.PERIODIC, callback=cb1_irq) 
t2.init(period=1400, mode=Timer.PERIODIC, callback=cb2_irq) 
