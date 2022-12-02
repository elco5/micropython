# https://docs.micropython.org/en/latest/wipy/tutorial/timer.html

from machine import Pin
from machine import Timer
from time import sleep_ms


class Pulser:


    # tim1 = Timer(1)
    tim2 = Timer(2)
    tim3 = Timer(3)



    def __init__(self, PULSER_PIN=32):

        self.PERIODIC_INTERVAL_MS = 327 # 15mph
        self.ON_TIME_MS = 20
        self.pulser_pin = Pin(PULSER_PIN, Pin.OUT)
  
    def pin_off(self,t):
        self.pulser_pin.value(0)


    def pin_on(self,t):
        '''callack to turn pin on for 100 ms'''
        self.pulser_pin.value(1)
        Pulser.tim3.init(period=self.ON_TIME_MS, mode=Timer.ONE_SHOT, callback=self.pin_off)


    def pass_pulse(self):
        '''non - callack to turn pin on for 100 ms'''
        self.pulser_pin.value(1)
        Pulser.tim3.init(period=self.ON_TIME_MS, mode=Timer.ONE_SHOT, callback=self.pin_off)
        print('pulse passed')


    def start_periodic(self):
        sleep_ms(280)
        print('delay 280 ms')
        Pulser.tim2.init(period=self.PERIODIC_INTERVAL_MS, mode=Timer.PERIODIC, callback=self.pin_on)
        print('pulser started')


    def stop_periodic(self):
        Pulser.tim2.deinit()
        self.pulser_pin.value(0)

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