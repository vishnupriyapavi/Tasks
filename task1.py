# task1:
# Q.write a prgm which will find all such a number which are divisible by 7 but are not a multiple of 5,between 2000
# and 3200(both included).the no obtained shpuld be printed in a comma separated sequence on a single line
# ans.1)
# def number():
#     for i in range(2000,3201):
#         if i%7==0 and i%5!=0:
#             print(i,end=",")
# number()
# ans.2)
# l=[]
# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         l.append(str(i))
# print(",".join(l))



# task2:
# Q.with a given integer number n,write a prgm to generate a dictionary that contain(i,i*i)such that is an integer number between
# 1 and n and the program should print the dict.suppose the following input is supplied to the prgm
# ex:8 output:{1:1,2:4,......}
# ans.)
# dic={}
# n=int(input("enter number:"))
# for i in range(1,n+1):
#     dic[i]=i*i
# print(dic)



# task3:
# Q.write a prgm which can compute factorial of agiven number the result should be printed in a comma separated sequence on a single lines.
# suppose the prgm input is supplied to the prgm
#ans)
# def fact():
#     f=1
#     n=int(input("Enter a number: "))
#     for i in range(1,n+1):
#         f=f*i
#     print(f)
# fact()




# task4:
# Q.write a prgm which accept a sequence of comma separated no frm console and generate a list a tuple which contain every no.
# a=input("enter numbers ")
# l=a.split(",")
# t=tuple(l)
# print(t)
# print(l)



# task5:
#Q. write a prgm that accepts asentance and calculate the number of upper case letter and lower case letter.
# ex:input:Hello world output:uppercase=1,lowercase=9
# uppercase=0
# lowercase=0
# a=input("enter a sentance: ")
# for i in a:
#     if i.isupper():
#         uppercase=uppercase+1
#     else:
#         lowercase=lowercase+1
# print("uppercase:",uppercase)
# print("lowercase:",lowercase)



# task6:
# Q.write a prgm that compute the net amount of a bank account based a transaction log from  console input.the transaction log format
# is shown as following D 100, W 200
# ex:d=100 d=100 w=100 d=200 out is 300
# Balance=0
# while True:
#     str=input("Deposit or withdraw(D or W)")
#     Transaction=str.split()
#     t=Transaction[0]
#     Amount=int(Transaction[1])
#     if t=='D':
#         Balance=Balance+Amount
#         print(Balance)
#     elif t=='W':
#         Balance =Balance - Amount
#         print(Balance)
#     else:
#         print("please enter valid choice:")
#     Exit=input("exit or continue(y or n)")
#     # if Exit!='y':
#         break

# another method:
# netamount=0
# while True:
#     s=input("no:")
#     if not s:
#         break
#     else:
#         value=s.split("")
#         operation=value[0]
#         amount=int(value[1])
#         if operation=="D":
#             netamount+=amount
#         elif operation=="W":
#             netamount-=amount
#         else:
#             pass
# print(netamount)



# task7:
# input value and that saved in list
# l=[]
# n=int(input("enter a value: "))
# for i in range(0,n):
#     value=input("enter values: ")
#     l.append(value)
# print(l)




# task8
# Q.array
# a=[]
# count=0
# arr=([1,2,1,1,3,5,6,8,125,4,1])
# print(arr)
# n=int(input("enter the value to check: "))
# for i in arr:
#     if i==n:
#         count=count+1
# print(count)
#


# task9:
# Q.define a fn that can accept 2 string as input and print the maximum length in console if the string are same lenth ,then
#  fn should print line by line
#
# def max(s1,s2):
#     # str1=input("Enter string1:")
#     # str2=input("Enter string2:")
#     l1=len(s1)
#     l2=len(s2)
#     if l1>l2:
#         print(s1)
#     elif l1<l2:
#         print(s2)
#     else:
#         print(s1)
#         print(s2)
# max("five","four")



# task10:
# Q.define a fn which can printa dict where the keys are no between 1 and 20(both are included)and value are squre of the key

# def dict1():
#     d={}
#     for i in range(1,21):
#         d[i]=i*i
#     print(d)
# dict1()



# task11:
# define a fn which can generate a list where the value are square a no between 1 and 20 (both include).then the fn need to print
# last 5 element in the list.

# def li():
#     l=[]
#     for i in range(1,21):
#         l.append(i*i)
#     print(l[-5:])
# li()
# output:[256, 289, 324, 361, 400]

# def li():
#     l=[]
#     for i in range(1,21):
#         l.append(i*i)
#     print(l[5:])
# li()
# output:
# [36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]




# task12:
# # Q.with a given tuple(1,2,3,4,5,6,7,8,9,10)write prgm to print the first half value in one line and last half value

# t=(1,2,3,4,5,6,7,8,9,10)
# print(t[:5])
# print(t[-5:])



# task13:
# Q.write a prgm which accepta string as input to print"yes" if the strring is "Yes"or YES or yes otherwise "no"
#
# n=input("enter a string:")
# if n=="yes" or n=="Yes" or n=="YES":
#     print("Yes")
# else:
#     print("No")




# task14:
# Q. write a prm which can filter even no in list using filter fn list[1,2,3,4,5,6,7,8,9,10]

# lis=[1,2,3,4,5,6,7,8,9,10]
# def even(x):
#     return x%2==0
# l2=list(filter(even,lis))
# print(l2)
# or
# lis=[1,2,3,4,5,6,7,8,9,10]
# even=filter(lambda x:x%2==0,lis)
# print(list(even))



# task15:
# Q.write a prgm to generate all sentance where subject is in ["i","you"]and the verb is in["play","love"]and th object is in
# ["hockey","football"]

# a=["i","you"]
# b=["play","love"]
# c=["hockey","football"]
# for x in a:
#     for y in b:
#         for z in c:
#             print(x,y,z)




# # lambda with fn examble :
# def maths(b):
#     return lambda a:a*(b*5)
# y=maths(6)
# print(y(7))



# task16:
# Q.Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five
# Input:[19, 19, 15, 5, 3, 5, 5, 2] Output:True

# n=int(input("enter range:"))
# l=[]
# for i in range(0,n):
#     a=int(input("enter a value:"))
#     l.append(a)
# print(l)
# if l.count(19)==2 and l.count(5)>=3:
#     print(True)
# else:
#     print(False)





# task17:
# Q. Write a Python program to find a pair with highest product from a given array of integers

# def max(a):
#     l=len(a)
#     x=a[0]
#     y=a[1]
#     for i in range(0,l):
#         for j in range(i+1,l):
#             if(a[i]*a[j]>x*y):
#                 x=a[i]
#                 y=a[j]
#     return x,y
# arr={1, 2, 3, 4, 7, 0, 8, 4}
# s=list(arr)
# print(arr)
# z=max(s)
# print(set(z))



# task18:
# Q.Write a Python program that accept a list of integers and check the length and the fifth element.
# Return true if the length of the list is 8 and fifth element occurs thrice in the said list.ex:19, 19, 15, 5, 5, 5, 1, 2 output:true
# 19, 15, 5, 7, 5, 5, 2output:false

# li=[]
# r=int(input("enter range:"))
# if r==8:
#     for i in range(0,r):
#         l=int(input("Enter values:"))
#         li.append(l)
#     print(li)
#     if li.count(li[4])==3:
#         print(True)
#     else:
#         print(False)
# else:
#     print("Error")


# TASK 19:
#Have the function ArrayChallenge(arr) take the array of numbers stored in arr which will contain integers that represent the amount
# in dollars that a single stock is worth,and return the maximum profit that could have been made by buying stock on day X and selling
# stock on day Y where Y>X .For example if array is [44,30,24,32,35,30,40,38,15] then your program should return 16 because at index
# 2 the stock was worth $24 and at index 6 the stock was then worth $40, so if you brought the stock at $24 and sold it at $40,
# you would have made a profit of $16,which is the maximum profit that could hve been made with this list of stock prices.
# If there is not profit that could have bveen made with the stock prices,then your program should return -1. For example arr is
# [10,9,8,2] then your program should return -1
# Example
# Input: [10,12,4,5,9]
# Output:5

# a=[10,12,4,5,9]
# n=len(a)
# b=[]
# for i in range(0,n):
#     for j in range(i+1,n):
#         if a[i]<a[j]:
#             p=a[j]-a[i]
#             b.append(p)
#         else:
#             b.append(-1)
# print(max(b))


# TASK 20:
#python prgm to display all integers within range 100 to 200 whose sum of digit is an even no
# l=[]
# for i in range(100,201):
#     i=str(i)
#     s=0
#     for j in i:
#         j=int(j)
#         s=s+j
#     if s%2==0:
#         l.append(i)
# print(l)


# TASK21
# python prgm to find largest no and position in a list without using bultin fn
li=[1,2,3,4,5,6,7,8,9]
# n=int(input("enter range: "))
# for i in range(0,n):
#     a=int(input("value: "))
#     li.append(a)
n=len(li)
max=li[0]
for i in range(0,n):
    if max<li[i]:
        max=li[i]
        p=i
print("maximum value is",max,"at",p)