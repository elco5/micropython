
from machine import WDT
from machine import Pin

from time import ticks_ms
from time import ticks_diff
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
SLEEP_TIME_MS = 20 # used as debounce time

# wdt = WDT(timeout=2000)  # enable it with a timeout of 2s
sens_led = Pin(LED_PIN, Pin.OUT)
state_led = Pin(STATE_LED_PIN, Pin.OUT, drive=Pin.DRIVE_3)
pulser = pulser.Pulser(PULSER_PIN=PULSER_PIN)
reed_switch = reed_switch.ReedSwitch(SENSOR_PIN=SENSOR_PIN)
tach = tach.Tach()
# disp = display.Display()
# state_machine = state_machine.StateMachine()

hack_mode = False
state_led.value(0)
verbose = True

this_loop_begin = ticks_ms()
print('starting sensor scan loop... Time: ', this_loop_begin)

while True:

    period = ticks_diff(ticks_ms(), this_loop_begin)
    this_loop_begin = ticks_ms()
    # wdt.feed()

    if reed_switch.closed:

        sens_led.on()
        
        tach.tic()

        '''pass pulse here if in passing mode '''
        if not hack_mode: pulser.pass_pulse()
        
        
        sleep_ms(SLEEP_TIME_MS)
        reed_switch.reset()

        sens_led.off()
        if verbose: tach.show()


        '''state transitions'''
        

    # transition from pass to hack
    if not hack_mode and tach.hi_speed:
        hack_mode = True
        state_led.on()
        pulser.start_periodic()
        print('hackin!')


    # transition from hack to pass
    if hack_mode and not tach.hi_speed:
        hack_mode = False
        state_led.off()
        pulser.stop_periodic()
        print('passing...')

    sleep_ms(5)

        # loop_time_end = ticks_ms()
        # print('loop_time', ticks_diff(loop_time_end, loop_time_begin))        