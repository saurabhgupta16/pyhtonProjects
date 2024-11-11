from clas_example import Calculator


class Science(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,2,10)

    def getfulldata(self):
        return self.num2 + self.num + self.age()



c = Science()
print(c.getfulldata())

