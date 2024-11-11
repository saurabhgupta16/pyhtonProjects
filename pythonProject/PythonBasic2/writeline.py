with open('test.txt','r' )as reader:
    content=reader.readlines()
    rcontent=reversed(content)
    with open('test.txt','w') as writer:

        for line in rcontent:
            writer.write(line)


with open('test.txt','r' ) as reader:
    content=reader.readlines()
    for i in content:
        print(i)