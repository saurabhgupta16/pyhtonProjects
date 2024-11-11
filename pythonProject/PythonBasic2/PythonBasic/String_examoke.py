'''
web = "saurabhgupta.com"
web1 = "someday something"
web2= "gupta"
for i in web:
    print(i)

print(web)
print(web[9])
print(web[0:7])
print(web + " " + web1)
print(web2 in web)

var=web.split(".")
print(var)
print(var[0])

web3= " James "
print(web3.strip())
print(web3.lstrip())
print(web3.rstrip())
'''
content="Please email us at mentor@rahulshettyacademy.com with below template to receive response"
print(content)
Var=content.split(" ")
print(Var)
for x in Var:
    if x=="mentor@rahulshettyacademy.com":
        y="mentor@rahulshettyacademy.com"
        break
print(y)