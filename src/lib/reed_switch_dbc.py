from machine import Pin
from machine import Timer
from machine import disable_irq
from machine import enable_irq
from time import sleep_ms
from time import ticks_ms
from time import ticks_diff

# https://docs.micropython.org/en/latest/reference/isr_rules.html#isr-rules
# https://techtutorialsx.com/2017/10/07/esp32-micropython-timer-interrupts/

DEBOUNCE_TIME_MS = 80


class ReedSwitch:

    def __init__(self, SENSOR_PIN):

        self.tim1 = Timer(1)

        self.switch = Pin(SENSOR_PIN, Pin.IN, Pin.PULL_UP)

        self.switch.irq(trigger=Pin.IRQ_FALLING,
                        handler=self.handle_interrupt)

        # initial state
        self.closed = False

    def debounce(self, t):
        if self.switch.value() == 0:
            self.closed = True

    def handle_interrupt(self, pin):

        # disable interrupts
        state = disable_irq()

        # wait debounce time
        self.tim1.init(period=DEBOUNCE_TIME_MS,
                       mode=Timer.ONE_SHOT,
                       callback=self.debounce)

        # re-enable irq
        enable_irq(state)

    def reset(self):

        self.closed = False


rs = ReedSwitch(SENSOR_PIN=25)
old = 0
while True:
    '''watch switch'''
    if rs.closed:
        dif = ticks_diff(ticks_ms(), old)
        old = ticks_ms()
        print('switch_closed: ', dif)
        rs.reset()
