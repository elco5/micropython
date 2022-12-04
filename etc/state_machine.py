
from collections import deque


class StateMachine():

    def __init__(self):

        self.state_hack = False
        self.q = deque((), maxlen=3)

    def set_input(self, bool: hi_speed):
        '''take tachometer data and add to input word'''
        self.q.append(hi_speed)

    def update_state(self):
        
        '''idea is to require 3 instances of state for state change'''
        if all(self.q): self.state_hack = True
        elif not any(self.q): self.state_hack = False  
        

