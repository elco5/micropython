
''' Pulse metering tachometer. 
Keeps the rolling average period of incomming pulses
Has a binary state (state_hi_speed) reflecting the  
pulse period with respect to a defined threshold
'''
from time import sleep_ms
from time import ticks_ms
from time import ticks_diff
from machine import Timer

from fifo_buffer import FIFOBuffer
from velo_calc import T_2_mph


timeout=Timer(0)


class Tach:

    def __init__(self, queue_size = 3):
        '''define time queue and track average
        keep speed state'''
        self.q = [5000] * queue_size
        self.buf = FIFOBuffer(size = 2)

        self.HI_SPEED_THRESHOLD_MS = 327 # 15 mph
        self.HI_SPEED_TIMEOUT_MS = 700
        self.hi_speed = False
        self.prev_pulse = ticks_ms()
        self.this_pulse = 0
        self.period = 0
        self.ave = 0


    def set_state(self):
        
        '''Add truth value of period being less than threshold'''
        self.buf.add_val(self.ave < self.HI_SPEED_THRESHOLD_MS)
        
        '''Flag to indicate speed is higher than threshold.'''
        self.hi_speed = self.buf.is_true()

        '''Flag will expire after timeout period'''
        if self.hi_speed: self.set_timer()


    def set_timer(self):
        # print('timeout_set')
        timeout.init(period=self.HI_SPEED_TIMEOUT_MS,
                        mode=Timer.ONE_SHOT,
                        callback=self.hi_speed_timeout)

    def hi_speed_timeout(self,t):
        self.hi_speed = False
        # print('hi_speed_timeout expired!')


    def take_record(self, now_ms):
        ''' add pulse time to queue'''
        self.q.append(now_ms)
        self.q = self.q[1:]


    def calc_rate(self):
        ''' update average of times in queue'''
        time_sum = 0
        for delt in self.q:
            time_sum += delt
        self.ave = int(time_sum/len(self.q))


    def calc_period(self):
        '''measure time between switch closures'''
        self.this_pulse = ticks_ms()
        self.period = ticks_diff(self.this_pulse, self.prev_pulse)
        self.prev_pulse = ticks_ms()
        return self.period  


    def tic(self):
        ''' record sensor event - calculate new sensor rate 
        - and set the hi_speed state variable'''
        self.take_record(self.calc_period())
        self.calc_rate()
        self.set_state()


    def show(self):
        d = {
            "ave": self.ave,
            "period": self.period,
            "hi_speed_state": self.hi_speed,
            "MPH": T_2_mph(self.ave)
            # "queue": self.q
            }
        print(ticks_ms(),':  ', d)
        # print(self.__dict__)





