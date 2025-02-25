class A:
    def setA(self,n1,n2,n3):
        self.n1=n1
        self.n2=n2
        self.n3=n3
n1=int(input("Enter the value of n1:-"))
n2=int(input("Enter the value of n2:-"))
n3=int(input("Enter the value of n3:-"))
class B(A):
    def setB(self,n1,n2,n3):
        print("Value of n1 is:-",self.n1)
        print("Value of n2 is:-",self.n2)
        print("Value of n3 is:-",self.n3)
class C(B):
    def setC(self,n1,n2,n3):
        if n1>n2 and n1>n3:
            print("n1 is Greater")
        elif n2>n1 and n2>n3:
            print("n2 is Greater")
        else:
            print("n3 is Greater")
c=C()
c.setA(n1,n2,n3)
c.setB(n1,n2,n3)
c.setC(n1,n2,n3)