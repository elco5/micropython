import uasyncio as asyncio
from primitives import Switch
from primitives import Delay_ms
from machine import Pin
from time import ticks_diff
from time import ticks_ms

var = 0


async def pulse(led, ms):
    print(var)
    led.on()
    await asyncio.sleep_ms(ms)
    led.off()

async def my_app():
    pin = Pin(25, Pin.IN, Pin.PULL_UP)  # Hardware: switch to gnd
    blue =Pin(2, Pin.OUT)
    sw = Switch(pin)
    sw.close_func(pulse, (blue, 100))  # Note how coro and args are passed
    await asyncio.sleep(60)  # Dummy application code

asyncio.run(my_app())  # Run main application code