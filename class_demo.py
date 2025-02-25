class Demo:
    def setData(self,name,email):
        self.name=name
        self.email=email
    def showData(self):
        print("Name is:-",self.name)
        print("Email is:-",self.email)
d=Demo()
name=input("Enter the Name:-")
email=input("Enter  the Email:-")
d.setData(name,email)
d.showData()