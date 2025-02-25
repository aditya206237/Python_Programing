class Demo:
    def __init__(self):
        print("Constructor is called")
    def setData(self,name,email):
        self.name=name
        self.email=email    
    def dhowData(self):
        print("Name=",self.name)
        print("Email=",self.email)
d=Demo()
name=input("Enter name:")
email=input("Enter email:")
d.setData(name,email)
d.dhowData()
# Output:
# Constructor is called
# Enter name:John
# Enter email: