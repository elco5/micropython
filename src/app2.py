

from machine import Pin
from time import sleep_ms
from time import ticks_ms
from time import ticks_diff

from lib import tach
from lib import pulser
from lib import reed_switch

LED_PIN = 32
SWITCH_PIN = 25
SLEEP_TIME_MS = 300

led = Pin(LED_PIN, Pin.OUT)
tach = tach.Tach()
pulser = pulser.Pulser(PULSER_PIN=2)
reed_switch = reed_switch.ReedSwitch(SWITCH_PIN)


prev_pulse = ticks_ms()


verbose = True
while True:
    
    if reed_switch.closed:
    # do things each switch closure
        # loop_time_begin = ticks_ms()
        # time critical tasks... 
        led.value(1)
        this_pulse = ticks_ms()
        period = ticks_diff(this_pulse, prev_pulse)
        prev_pulse = ticks_ms()
        # end time critcal tasks...

        print('Pulse Detected!')
        tach.record(period)
        sleep_ms(SLEEP_TIME_MS)
        led.value(0)
        
        if verbose: tach.show()


        reed_switch.reset()
        # loop_time_end = ticks_ms()
        # print('loop_time', ticks_diff(loop_time_end, loop_time_begin))

    # if not tach.hi_speed:
    #     pulser.pass_pulse()
    #     pass # pass the pulse
    # else:
    #     # high speed state == True
    #     pass # 16 mph pulse 

    