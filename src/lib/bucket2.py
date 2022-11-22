

class Bucket:
    size = 3
    
    avg = 0

    def __init__(self) -> None:

        self.d = [0, 0, 0,]

    def push(self, val):
        self.d[1,:]
        self.d.append(val)
        self.avg = self.compute_ave_deque()      

    def compute_ave_deque(self):
        sum = 0
        for num in self.d:
            sum = sum + num
        return int(sum/len(self.d))
    
    def show(self):
        str_d = ''
        for i in range(self.size):
            str_d = str_d + str(self.d(i)) + ' '
        
        print('[' , str_d, 'avg: ', self.avg, ']')

b = Bucket()
b.show()
# b.push(6)
# b.show()
# print(b.avg)
# b.push(6)
# b.show()
# print(b.avg)
# b.push(6)
# b.show()
# print(b.avg)

