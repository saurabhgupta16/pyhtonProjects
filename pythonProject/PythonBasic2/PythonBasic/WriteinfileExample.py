with open('test.txt', 'r') as file:
    content = file.readlines()
    rc = reversed(content)
    with open('test.txt', 'w') as nfile:
        for i in rc:
            nfile.write(i)

with open('test.txt', 'r') as l:
    for j in l.readlines():
        print(j)
