class Parent:
    def setParent(self,n1,n2):
        self.n1=n1
        self.n2=n2
n1=int(input("Enter the value of n1:-"))
n2=int(input("Enter the value of n2:-"))
class Child(Parent):
    def setChild(self,n1,n2):
        print("Value of n1 is:-",self.n1)
        print("Value of n2 is:-",self.n2)
        print("Adddition is :-", self.n1+self.n2)

c=Child()
c.setParent(n1,n2)
c.setChild(n1,n2)