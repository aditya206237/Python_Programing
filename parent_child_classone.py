class Parent:
    def setParent(self):
        print("This is a Parent Class")
class Child(Parent):
    def setChild(self):
        print("This is a Child Class")

c=Child()
c.setParent()
c.setChild()