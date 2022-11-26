# https://docs.micropython.org/en/latest/wipy/tutorial/timer.html

from machine import Pin
from machine import Timer

class Pulser:


    # tim1 = Timer(1)
    tim2 = Timer(2)
    tim3 = Timer(3)


    def __init__(self, PULSER_PIN=32):

        self.pin = Pin(PULSER_PIN, Pin.OUT)

  
    def pin_off(self,t):
        self.pin.value(0)


    def pin_on(self,t):
        '''callack to turn pin on for 100 ms'''
        self.pin.value(1)
        Pulser.tim3.init(period=100, mode=Timer.ONE_SHOT, callback=self.pin_off)


    def pass_pulse(self):
        '''non - callack to turn pin on for 100 ms'''
        self.pin.value(1)
        Pulser.tim3.init(period=100, mode=Timer.ONE_SHOT, callback=self.pin_off)
        print('pulse passed')


    def start_periodic(self):
        Pulser.tim2.init(period=1500, mode=Timer.PERIODIC, callback=self.pin_on)
        print('pulser started')


    def stop_periodic(self):
        Pulser.tim2.deinit()
        self.pin.value(0)

'''
>>> import pulser as p
>>> m = p.Pulser()
>>> m.start()
pulser started
>>> m.stop()
>>> m.pass_pulse()
pulse passed
>>> m.pass_pulse()
pulse passed
>>>
'''