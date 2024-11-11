a=0
if a!=2:
    pass
#   raise Exception("I am in fail part")
assert (a==0)

try:
    with open('test.txt', 'r') as reader:
        print(reader.read())
except:
    print("I am able to catch the file open error")

try:
    with open('file.txt', 'r') as reader:
        print(reader.read())
except Exception  as E:
        print(E)

finally:
        print("I am a Cleaner")