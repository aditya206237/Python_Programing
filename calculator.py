n1=int(input("Enter the value of n1:-"))
n2=int(input("Enter the value of n2:-"))
print("For addition enter choice==> 1")
print("For subtraction enter choice==> 2")
print("For multiplication enter choice==> 3")
print("For division enter choice==> 4")
choice=int(input("Enter the choice:-"))
if choice==1:
    add=n1+n2
    print("Addition is:-",add)
elif choice==2:
    subtract=n1-n2
    print("Subtraction is:-",subtract)
elif choice==3:
    multiply=n1*n2
    print("Multiplication is:-",multiply)
elif choice==4:
        if n2==0:
          print("Can't Divide to zero")
        else:
          divide=n1/n2
          print("Division is:-",divide)
else:
    print("Invalid")
    