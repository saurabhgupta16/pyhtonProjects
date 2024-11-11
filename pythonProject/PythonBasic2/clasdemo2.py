class cal:
    num = 200

    def __init__(self,a,b):

        print("I am in Default Constructor in Parent class")
        self.fnumber = a
        self.lnumber = b

    def iadd(self):

        c = self.fnumber+self.lnumber+cal.num
        return c

obj = cal(2, 4)
print(obj.num)
print(obj.iadd())


