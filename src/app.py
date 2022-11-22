

from machine import Pin
from time import sleep_ms
from time import ticks_ms
from time import ticks_diff

from lib import bucket

LED_PIN = 32
SWITCH_PIN = 25
SLEEP_TIME_MS = 300


led = Pin(LED_PIN, Pin.OUT)
switch = Pin(SWITCH_PIN, Pin.IN, Pin.PULL_UP)
bucket = bucket.Bucket(3)


def handle_interrupt(pin):
    global switch_closed
    switch_closed = True

switch.irq(trigger=Pin.IRQ_FALLING,
           handler=handle_interrupt)

prev_pulse = ticks_ms()


switch_closed = False
while True:

    if switch_closed:
        led.value(1)

        this_pulse = ticks_ms()
        period = ticks_diff(this_pulse, prev_pulse)
        bucket.push(period)
        prev_pulse = ticks_ms()

        print(f'Pulse Detected! - Time: \
            this: {this_pulse},\
            prev: {prev_pulse},\
            period = {period} ms')
        
        bucket.show()

        sleep_ms(SLEEP_TIME_MS)
        led.value(0)
        print('Waiting...')

        switch_closed = False
