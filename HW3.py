import re

p = input("Enter password: ")
x = True
while x:
    if (len(p)<8 or len(p)>15):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[!@#$%^&*()_+={}|\";'<>,.?/~`]", p):
        break
    elif re.search("\s", p):
        break
    else:
        print("Valid Password")
        x = False
        break

if x:
    print("Not a Valid Password")



