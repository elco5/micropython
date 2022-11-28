
from machine import WDT
from machine import Pin
from time import sleep_ms

from lib import tach
from lib import pulser
from lib import reed_switch
from lib import state_machine

LED_PIN = 32
STATE_LED_PIN = 5
PULSER_PIN = 2
SWITCH_PIN = 25
SLEEP_TIME_MS = 300

# wdt = WDT(timeout=2000)  # enable it with a timeout of 2s
led = Pin(LED_PIN, Pin.OUT)
state_led = Pin(STATE_LED_PIN, Pin.OUT)
pulser = pulser.Pulser(PULSER_PIN=PULSER_PIN)
reed_switch = reed_switch.ReedSwitch(SWITCH_PIN=SWITCH_PIN)
tach = tach.Tach()
# state_machine = state_machine.StateMachine()

hack_mode = False
verbose = True


while True:
    # wdt.feed()

    if reed_switch.closed:
        
        # loop_time_begin = ticks_ms()
        # do things each switch closure
        led.value(1)
        tach.tic()

        '''pass pulse here if in passing mode '''
        if not hack_mode: pulser.pass_pulse()
        
        sleep_ms(SLEEP_TIME_MS)
        reed_switch.reset()
        led.value(0)
        if verbose: tach.show()


        '''state transitions'''
        

    # transition from pass to hack
    if not hack_mode and tach.hi_speed:
    
        hack_mode = tach.hi_speed
        pulser.start_periodic()
        
        state_led.value(1)
        print('we hackin!')


    # transition from hack to pass
    if hack_mode and not tach.hi_speed:
    
        hack_mode = tach.hi_speed
        pulser.stop_periodic()

        state_led.value(hack_mode)
        print('passin...')

    sleep_ms(100)

        # loop_time_end = ticks_ms()
        # print('loop_time', ticks_diff(loop_time_end, loop_time_begin))

 