import uasyncio as asyncio
from primitives import Switch
from primitives import Delay_ms
from machine import Pin
from time import ticks_diff
from time import ticks_ms



async def foo(evt):
    print('foo called..')
    while True:
        evt.clear()  # re-enable the event
        await evt.wait()  # minimal resources used while paused
        print("Switch closed.")
        # Omitted code runs each time the switch closes

async def main():
    print('sync.py main running..')
    sw = Switch(Pin(25, Pin.IN, Pin.PULL_UP))
    sw.close_func(None)  # Use event based interface
    # sw.open_func(None)  # Use event based interface
    await foo(sw.close)  # Pass the bound event to foo
    # await foo(sw.close)  # Pass the bound event to foo

asyncio.run(main())