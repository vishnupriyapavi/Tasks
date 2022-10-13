# def first():
#     print("hello")
# first()

# def fun1(name):
#     # print("hello",name)
#     print(name+ " hai")
# fun1("vishnupriya")

# def fun2(fname,lname):
#     print("haii",fname,lname)
#     lname=input("enter lname:")
# fun2("aaa","bbb")

# def fun3(*names):
#     print("good person is "+ names[2])
# fun3("aaa","bbb","ccc","ddd")

# keyword arguments
# def fun4(child1,child2,child3):
#     print("the smallest person",child2)
# fun4(child1="qwe",child2="wsx",child3="edc")

# arbitary keyword arguments(**kwargs)
def fun5(**child):
    print("smallest child is " + child["child2"])
fun5(child1="qwe",child2="asd",child3="zxc")