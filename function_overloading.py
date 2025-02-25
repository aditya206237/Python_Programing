class Demo:
    def areaCircle(self,r):
        self.r=r
        self.ciircle=3.14*r*r
        print("Area of Circle=",self.ciircle)
    def area(self,r,h):
        self.h=h
        self.r=r
        self.cylinder=3.14*r*r*h
        print("Area of Cylinder=",self.cylinder)

d=Demo()
r=float(input("Enter radius:"))
h=float(input("Enter height:"))
d.area(r,h)
d.areaCircle(r)