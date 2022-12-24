from machine import Pin
import uasyncio as asyncio

from primitives import Switch

class EV_switch:

    def __init__(self, pin):

        self.sw = Switch(Pin(pin), Pin.IN, Pin.PULL_UP)
        self.sw.close_func(None) # close func will be an event
