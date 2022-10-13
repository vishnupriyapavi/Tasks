username=["vishnupriya","vismaya","sreema"]
password=[123,456,789]

name=input("Enter your usename: ")
if name in username:
    pass1= (input("enter your password: "))
    a=username.index(name)
    if pass1 in password and a==password.index(pass1):
        print("Welcome")
    else:
        print("invalid password")
else:
    print("invalid username")