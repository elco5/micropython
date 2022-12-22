import uasyncio as asyncio
from primitives import Switch
from primitives import Delay_ms
from machine import Pin
from time import ticks_diff
from time import ticks_ms

var = 0
start_time = 0


async def pulse_begin_0(led, ms):
    led.on()

    print('begin')
    # start_time = 'spam'
    start_time = ticks_ms()
    print(start_time)
    await asyncio.sleep_ms(ms)
    
    led.off()

async def pulse_begin():

    start_time = 'spam'
    print(start_time)

async def pulse_end():

    start_time = 'set to eggs'
    print(start_time)

    # period = ticks_diff(ticks_ms(), 0)
    
    # print('period:', period)
    


async def my_app():
    pin = Pin(25, Pin.IN, Pin.PULL_UP)  # Hardware: switch to gnd
    sw = Switch(pin)

    blue =Pin(2, Pin.OUT)
    
    sw.open_func(pulse_begin)  # Note how coro and args are passed
    sw.close_func(pulse_end)  # Note how coro and args are passed
    
    await asyncio.sleep(60)  # Dummy application code

asyncio.run(my_app())  # Run main application code