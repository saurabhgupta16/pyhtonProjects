from PythonBasic2.clasdemo2 import cal

class ChildImp(cal):
    num2 = 900

    def __init__(self,c,d):
        self.number1 = c
        self.number2 = d
        print("I m in child Constructor")
        cal.__init__(self,2,10)

    def getData(self):
        print("I am in getdata")
        return self.num2+self.num+self.iadd()


    def subs(self):
        print("I am in Subs")
        return self.number1-self.number2

obj=ChildImp(1,3)

print(obj.getData())

print(obj.subs())

print(obj.num2)