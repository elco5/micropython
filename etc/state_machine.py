
class StateMachine():
    
    def __init__(self):

        self.state_hack = False #starting state
        self.input_hi_speed = False
    
    
    def take_input(self, bool: hi_speed):
        
        self.input_hi_speed = hi_speed
    

    def update_state(self):
        
        if self.input_hi_speed: 
            self.state_hack = True


                    
        




    

