class Employee:
    def setData(self,name,no,bsal):
        self.name=name
        self.no=no
        self.bsal=bsal
    def calculation(self):
        self.da=self.bsal*0.2
        self.hra=self.bsal*0.5
        self.pf=self.bsal*0.1
        self.total=self.bsal+self.da+self.hra-self.pf
    def showData(self):
        print("Name of Employee:-",self.name)
        print("No of Employe:-",self.no)
        print("Basic salary:-",self.bsal)
        print("Da is:-",self.da)
        print("Hra is:-",self.hra)
        print("Pf is:-",self.pf)
        print("Total is:-",self.total)
name=(input("Name of Employee:-"))
bsal=int(input("Enter Basic Salary:-"))
no=(input("Enter the number of Employee:-"))
e=Employee()
e.setData(name,no,bsal)
e.calculation()
e.showData()