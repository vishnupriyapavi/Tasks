a=str(input("enter a string"))
rev=""
for i in a:
    rev=i+rev
if a==rev:
    print("palindrome")

else:
    print("not palindrome")
