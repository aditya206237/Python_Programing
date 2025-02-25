no=int(input("Enter the number:-"))
num=0
while no>0:
    num=int(num*10)+(no%10)
    no=int(no/10)
print(num)