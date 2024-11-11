file = open('test.txt')
#print(file.read())
'''print(file.readline())
print(file.readline())
print(file.readline())

# reading all the lines in File 
l=file.readline()
while l !='':
    print(l)
    l = file.readline()'''

#Readlines Function store the DAta in a list which is easy to Looped through
line=file.readlines()
for i in line:
    print(i)
file.close()

