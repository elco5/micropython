
from machine import WDT
from machine import Pin
from time import sleep_ms

from lib import display
from lib import tach
from lib import pulser
from lib import reed_switch
from lib import state_machine

LED_PIN = 2
STATE_LED_PIN = 5
PULSER_PIN = 32
SENSOR_PIN = 25
SLEEP_TIME_MS = 100 # used as debounce time

# wdt = WDT(timeout=2000)  # enable it with a timeout of 2s
led = Pin(LED_PIN, Pin.OUT)
state_led = Pin(STATE_LED_PIN, Pin.OUT)
pulser = pulser.Pulser(PULSER_PIN=PULSER_PIN)
reed_switch = reed_switch.ReedSwitch(SENSOR_PIN=SENSOR_PIN)
tach = tach.Tach()
# disp = display.Display()
# state_machine = state_machine.StateMachine()

hack_mode = False
state_led.value(0)
verbose = True

print('starting sensor scan loop...')
while True:
    # wdt.feed()

    if reed_switch.closed:
        
        # loop_time_begin = ticks_ms()
        # do things each switch closure
        led.value(1)
        
        tach.tic()


        '''pass pulse here if in passing mode '''
        if not hack_mode: pulser.pass_pulse()
        
        # ''' display stuff '''
        # disp.oled.show()
        # disp.show_number(tach.period)
        
        sleep_ms(SLEEP_TIME_MS)
        reed_switch.reset()

        led.value(0)
        if verbose: tach.show()


        '''state transitions'''
        

    # # transition from pass to hack
    # if not hack_mode and tach.hi_speed:
    #     print()
    #     pulser.start_periodic()
    #     hack_mode = True
    #     state_led.value(1)

    #     print('hackin!')


    # # transition from hack to pass
    # if hack_mode and not tach.hi_speed:
    
    #     pulser.stop_periodic()
    #     hack_mode = False
    #     state_led.value(0)

    #     print('passing...')

    # sleep_ms(100)

        # loop_time_end = ticks_ms()
        # print('loop_time', ticks_diff(loop_time_end, loop_time_begin))        