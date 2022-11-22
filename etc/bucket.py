from collections import deque

class Bucket:
  
    d = deque()
    avg = 0

    def __init__(self, maxlen=3) -> None:
        
        empty_deque = []
        for i in range(maxlen):
            empty_deque.append(0)

        self.d = deque(empty_deque, maxlen = maxlen)

    def push(self, val):

        self.d.append(val)
        self.avg = self.compute_ave_deque()      

    def compute_ave_deque(self):
        sum = 0
        for num in self.d:
            sum = sum + num
        return int(sum/len(self.d))
    
    def show(self):
        print('[' , *self.d, 'avg: ', self.avg, ']')

# b = Bucket(3)
# b.show()
# b.push(6)
# b.show()
# print(b.avg)
# b.push(6)
# b.show()
# print(b.avg)
# b.push(6)
# b.show()
# print(b.avg)

