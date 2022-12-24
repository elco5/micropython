
import uasyncio as asyncio
from machine import Pin

from time import ticks_ms
from time import ticks_diff
from time import sleep_ms

from lib import display
from lib import tach
from lib import pulser
from primitives import Switch
# from lib import reed_switch

LED_PIN = 2
STATE_LED_PIN = 5
PULSER_PIN = 32
SENSOR_PIN = 25
SLEEP_TIME_MS = 20 # used as debounce time

# wdt = WDT(timeout=2000)  # enable it with a timeout of 2s
sens_led = Pin(LED_PIN, Pin.OUT)
state_led = Pin(STATE_LED_PIN, Pin.OUT, drive=Pin.DRIVE_3, value=1)
pulser = pulser.Pulser(PULSER_PIN=PULSER_PIN)
tach = tach.Tach()


sw = Switch(Pin(25, Pin.IN, Pin.PULL_UP))
sw.close_func(None)  # Use event based interface


hack_mode = False
state_led.value(0)
verbose = True

this_loop_begin = ticks_ms()

def switch_close_duties():
    # tach.tic()
    # if not hack_mode: 
    pulser.pass_pulse()
    # if verbose: tach.show()

async def switch_close_event(evt):
    while True:
        evt.clear()  # re-enable the event
        await evt.wait()  # minimal resources used while paused
        print("Switch closed.")
        switch_close_duties()
           

async def main_loop():
    await switch_close_event(sw.close)

asyncio.run(main_loop())




    # while True:

    #     period = ticks_diff(ticks_ms(), this_loop_begin)
    #     this_loop_begin = ticks_ms()
    #     # wdt.feed()

    #     if reed_switch.closed:

    #         sens_led.on()
            
    #         tach.tic()

    #         '''pass pulse here if in passing mode '''
    #         if not hack_mode: pulser.pass_pulse()
            
            
    #         sleep_ms(SLEEP_TIME_MS)
    #         reed_switch.reset()

    #         sens_led.off()
    #         if verbose: tach.show()


    # '''state transitions'''
        

    # # transition from pass to hack
    # if not hack_mode and tach.hi_speed:
    #     hack_mode = True
    #     state_led.on()
    #     pulser.start_periodic()
    #     print('hackin!')


    # # transition from hack to pass
    # if hack_mode and not tach.hi_speed:
    #     hack_mode = False
    #     state_led.off()
    #     pulser.stop_periodic()
    #     print('passing...')

    # sleep_ms(5)

        # loop_time_end = ticks_ms()
        # print('loop_time', ticks_diff(loop_time_end, loop_time_begin))        