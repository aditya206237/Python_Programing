class Demo:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def showData(self):
        print("Name=",self.name)
        print("Email=",self.email)

name=input("Enter name:")   