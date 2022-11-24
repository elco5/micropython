
''' Pulse metering. 
Keeps the rolling average period of incomming pulses
Has a binary state (state_hi_speed) reflecting the  
pulse period with respect to a defined threshold
'''


class Tach:

    def __init__(self, queue_size):
        '''define time queue and track average
        keep speed state'''
        self.THRESHOLD = 2000       
        self.hi_speed = False
        self.q = [5000] * queue_size
        self.rate = 0

    def set_state(self):
        self.hi_speed = (self.rate < self.THRESHOLD)

    def record(self, millisecond_time):
        ''' add pulse time to queue'''
        self.q.append(millisecond_time)
        self.q = self.q[1:]
        self.set_rate()
        self.set_state()

    def set_rate(self):
        ''' update average of times in queue'''
        time_sum = 0
        for delt in self.q:
            time_sum += delt
        self.rate = int(time_sum/len(self.q))

    def show(self):
        ''' print the Tach instance dictionary'''
        print(self.__dict__)

