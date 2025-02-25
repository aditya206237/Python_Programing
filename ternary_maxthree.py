n1=int(input("Enter the value of n1:-"))
n2=int(input("Enter the value of n2:-"))
n3=int(input("Enter the value of n3:-"))
check=(n1 if n1>n2 else n2) if (n1 if n1>n2 else n2)>n3 else n3
check1=n1 if n1>n2 and n1>n3 else n2 if n2>n3 else n3
print("Max is",check)
print("Max is",check1)