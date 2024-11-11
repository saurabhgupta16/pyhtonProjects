file = open('test.txt')
#print(file.read(3))
#print(file.readline())
#print(file.readline())

#line=file.readline()
#while line != "":
#    print(line)
#    line=file.readline()

#line = file.readlines()
#for i in line:
#    print(i)

with open('test.txt','r') as reader:
    content=reader.readlines()
    with open('test.txt','w')  as writer:
        for i in reversed(content):
            writer.write(i)


#file.close()