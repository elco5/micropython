

from machine import Pin
from time import sleep_ms
from time import ticks_ms
from time import ticks_diff

from lib import tach

LED_PIN = 32
SWITCH_PIN = 25
SLEEP_TIME_MS = 300

real_speed_low = True
led = Pin(LED_PIN, Pin.OUT)
switch = Pin(SWITCH_PIN, Pin.IN, Pin.PULL_UP)
tach = tach.Tach(3)

verbose = True


def handle_interrupt(pin):
    global switch_closed
    switch_closed = True 
    # do things each switch closure

# configure interrupt on switch pin
switch.irq(trigger=Pin.IRQ_FALLING,
           handler=handle_interrupt)

prev_pulse = ticks_ms()


switch_closed = False
while True:
    
    if switch_closed:
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
        print('Waiting...')

        switch_closed = False
        # loop_time_end = ticks_ms()
        # print('loop_time', ticks_diff(loop_time_end, loop_time_begin))

    if not tach.hi_speed:
        # pulser.pass_pulse()
        pass # pass the pulse
    else:
        # high speed state == True
        pass # 16 mph pulse 