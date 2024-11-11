class Calculator:
    num = 100

    def __init__(self, a, b):
        self.fnum = a
        self.snum = b
        print("I am in Contractor")



    def age(self):
         return self.fnum + self.snum + self.num


    def fullname(self):
        print("My name saurabh ")


c = Calculator(2, 3)
print(c.age())
c.fullname()


d = Calculator(5, 10)
print(d.age())
d.fullname()