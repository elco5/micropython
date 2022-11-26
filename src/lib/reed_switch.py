from machine import Pin
from machine import Timer
# https://docs.micropython.org/en/latest/reference/isr_rules.html#isr-rules
# https://techtutorialsx.com/2017/10/07/esp32-micropython-timer-interrupts/
class ReedSwitch:



    def __init__(self, SWITCH_PIN):
        
        self.switch = Pin(SWITCH_PIN, Pin.IN, Pin.PULL_UP)

        self.switch.irq(trigger=Pin.IRQ_FALLING,
               handler=self.handle_interrupt)

        self.closed = False

        self.debounce_timeout = False
    
    def handle_interrupt(self, pin):
        
        self.closed =  True


    def reset(self):

        self.closed = False

    