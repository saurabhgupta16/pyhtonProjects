file=open('test.txt')
#print(file.read())  # read whole file
#print(file.read(5))  #read only limited Cahracter
#print(file.readline())

#line=(file.readline())
#while line != "":
#    print(line)
#    line=file.readline()


lines = file.readlines()
for i in lines:

        print(i)

file.close()