# https://docs.micropython.org/en/latest/wipy/tutorial/timer.html

from machine import Pin
from machine import Timer

class Pulser:

    PULSER_PIN = 32
    # tim1 = Timer(1)
    tim2 = Timer(2)
    tim3 = Timer(3)


    def __init__(self):

        self.pin = Pin(Pulser.PULSER_PIN, Pin.OUT)

        # self.tim1 = Pulser.tim1.init(period=5000, mode=Timer.PERIODIC,
        #     callback=lambda t:print("Welcome to Microcontrollerslab"))

    def pass_pulse(self):

        self.pin.value(1)
        Pulser.tim3.init(period=100, mode=Timer.ONE_SHOT, callback=self.pulser_off)
        print('pulse passed')

    def hack_speed(self):
        self.start()       


    def pulser_off(self,t):
        self.pin.value(0)
        # print('pin off')

    def pulser_on(self,t):
        self.pin.value(1)
        Pulser.tim3.init(period=100, mode=Timer.ONE_SHOT, callback=self.pulser_off)
        # print('pin on')

    def start(self):
        Pulser.tim2.init(period=1000, mode=Timer.PERIODIC, callback=self.pulser_on)
        print('pulser started')

    def stop(self):
        Pulser.tim2.deinit()

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