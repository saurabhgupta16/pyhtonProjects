try:
    with open('testlog.txt', 'r') as reader:
        reader.read()
except:
    print("I am in catch block")

try:
    with open('testlog.txt', 'r') as reader:
            reader.read()
except Exception  as e:
        print(e)
        print(" this is fail becuase file name is not Exist")
