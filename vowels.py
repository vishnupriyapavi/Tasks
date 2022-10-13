paragraph=str(input("paragraph"))
vowels=('a','e','i','o','u')
count=0
for i in paragraph:
    if i in vowels:
        count=count+1
if count!=0:
    print("no of vowels:",count)
else:
    print("no vowels occur")
