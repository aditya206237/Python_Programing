def myFun(x):
    num=0
    while x>0:
        num= int(num*10) + int(x%10)
        x=int(x/10)
    print(num)
myFun(123)
