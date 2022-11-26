
''' Pulse metering tachometer. 
Keeps the rolling average period of incomming pulses
Has a binary state (state_hi_speed) reflecting the  
pulse period with respect to a defined threshold
'''
from time import sleep_ms
from time import ticks_ms
from time import ticks_diff
from machine import Timer


timeout=Timer(1)


class Tach:

    def __init__(self, queue_size = 3):
        '''define time queue and track average
        keep speed state'''
        self.q = [5000] * queue_size
        # time deltas below this ms value trigger hi speed state 
        self.HI_SPEED_THRESHOLD_MS = 2000
        self.HI_SPEED_TIMEOUT_MS = 3000
        self.hi_speed = False
        self.prev_pulse = ticks_ms()
        self.this_pulse = 0
        self.period = 0
        self.rate = 0


    def set_state(self):
        '''Flag to indicate speed is higher than threshold.
        Flag will expire after timeout period'''
        self.hi_speed = (self.rate < self.HI_SPEED_THRESHOLD_MS)
        # set timeout on hi-speed state
        if self.hi_speed:
            print('timeout_set')
            timeout.init(period=self.HI_SPEED_TIMEOUT_MS,
                         mode=Timer.ONE_SHOT,
                         callback=self.hi_speed_timeout)

    def hi_speed_timeout(self,t):
        self.hi_speed = False
        print('hi_speed_timeout expired!')


    def take_record(self, now_ms):
        ''' add pulse time to queue'''
        self.q.append(now_ms)
        self.q = self.q[1:]


    def calc_rate(self):
        ''' update average of times in queue'''
        time_sum = 0
        for delt in self.q:
            time_sum += delt
        self.rate = int(time_sum/len(self.q))


    def calc_period(self):
        '''measure time between switch closures'''
        self.this_pulse = ticks_ms()
        self.period = ticks_diff(self.this_pulse, self.prev_pulse)
        self.prev_pulse = ticks_ms()
        return self.period  


    def tic(self):
        self.take_record(self.calc_period())
        self.calc_rate()
        self.set_state()


    def show(self):
        d = {
            "rate": self.rate,
            "period": self.period,
            "hi_speed_state": self.hi_speed
            # "queue": self.q
            }
        print(d)





