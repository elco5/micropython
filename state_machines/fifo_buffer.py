

class FIFOBuffer():

    def __init__(self, size = 8):
        self.buf = [False]* size
        pass

    def add_val(self, val):
        ''' add value to buffer'''
        ''' drop leftmost buffer value'''
        self.buf.append(val)
        self.buf = self.buf[1:]

    def is_true(self):
        # return true if all are true
        print('testing:', *self.buf)
        for val in self.buf:
            print('this val: ', val)
            if val == False:
                print(val)
                return False    
        return True
    
    def show(self):
        print('buf: ' , *self.buf)


rb  = FIFOBuffer()

rb.show()
rb.add_val(True)
rb.add_val(True)
rb.add_val(True)
rb.add_val(True)
rb.show()
print(rb.is_true())
print()
rb.add_val(True)
rb.add_val(True)
rb.add_val(True)
rb.add_val(True)
rb.show()
print(rb.is_true())
rb.add_val(False)
rb.show()
print(rb.is_true())
