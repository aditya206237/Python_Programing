n1=0
n2=1
print(n1,n2,sep=",",end=",")
i=1
while i<=5:
    n3=n1+n2
    print(n3,end=",")
    n1=n2
    n2=n3
    i=i+1
