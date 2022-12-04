
class SM:
    
    def start(self):
        self.state = self.startState
    
    def step(self, inp):
        (s, o) =  self.getNextValues(self.state, inp)
        self.state = s
        print('out: ', o)
        return o

    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]

    
class Accumulator(SM):
    startState = 0
    def getNextValues(self, state, inp):
        return (state + inp, state + inp)

class RingBuffer(SM):
    pass

a =  Accumulator()
a.start()
a.step(3)
a.step(4)
a.step(-2)
a.transduce([100, -3, 4, -123, 10])