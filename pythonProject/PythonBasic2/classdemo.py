class calCulator:
    num = 100

    def __init__(self):
        print("i am called from the default construction when object of that class being created")
    def greetme(self):
        print("I am inside the Greet Method")


obj = calCulator()
obj.greetme()
a,b = obj.num,obj.num
print(a+b)

