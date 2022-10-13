# def prime():
#     n=int(input("Enter a number:"))
#     for i in range(2,n):
#         if n%i!=0:
#             print("true")
#         else:
#             print("false")
# prime()
def prime(n):
    for i in range(2,n):
        if n%i!=0:
            print(True)
            break
        else:
            print(False)
            break
prime(5)