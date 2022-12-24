import uasyncio as asyncio
from machine import Pin
from time import ticks_diff
from time import ticks_ms

from primitives import Switch
from primitives import Delay_ms

start = 0
diff = 0


def disp_diff():
    diff = ticks_diff(ticks_ms(), start)
    print('set diff: ', diff)


def set_start():
    global start
    start = ticks_ms()
    print('set start: ', start)


async def foo(evt):

    while True:
        evt.clear()  # re-enable the event
        await evt.wait()  # minimal resources used while paused
        print("Switch closed.")

        disp_diff()  # calculate and display time delta since last closure

        set_start()  # update time of switch closure



async def main():
    print('sync.py main running..')
    sw = Switch(Pin(25, Pin.IN, Pin.PULL_UP))
    sw.close_func(None)  # Use event based interface
    await foo(sw.close)  # Pass the bound event to foo


asyncio.run(main())
