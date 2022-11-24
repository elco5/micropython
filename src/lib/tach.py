
''' low level metering of pulses
keeps rolling average of the period
of incomming pulses'''

class Tach:

    def __init__(self, window):
        '''define time queue and track average'''
        self.Q = [0] * window
        self.avg = 0


    def pulse(self, millisecond_time):
        ''' add pulse time to queue'''
        self.Q = [millisecond_time, *self.Q[:-1]]

        self.set_rate()
        
    def set_rate(self):
        
        time_sum = 0
        
        for delt in self.Q:
            time_sum += delt

        self.avg = int(time_sum/len(self.Q))

        
# from tach import Tach
t = Tach(3)
print(t.__dict__)
t.pulse(55)
print(t.__dict__)
t.pulse(66)
print(t.__dict__)
t.pulse(77)
print(t.__dict__)
t.pulse(88)
print(t.__dict__)
rate = t.pulse(99)
print(t.__dict__)
print(rate)
