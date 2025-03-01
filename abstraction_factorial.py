class Parent:
    def showData(self,no):
        pass
class Child(Parent):
    def showData(self,no):
        self.fact=1
        self.no=no
        while self.no>0:
            self.fact=self.fact*self.no
            self.no=self.no-1
        print("Factorial is:",self.fact)

no=int(input("Enter the value of number:-"))
c=Child()
c.showData(no)