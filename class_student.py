class Student:
    def setData(self,name,number,maths,english,gujrati):
        self.name=name
        self.number=number
        self.maths=maths
        self.english=english
        self.gujrati=gujrati
    def Calculation(self):
        self.addition=self.maths+self.english+self.gujrati
        self.division=self.addition / 300
        self.per=self.division * 100
    def Grade(self):
        if float(self.per>=80) and float(self.per<=100):
          print("Distinction")
        elif float(self.per>=60) and float(self.per<=79):
          print("First Class")
        elif float(self.per>=50) and float(self.per<=59):
          print("Second Class")
        elif float(self.per>=40) and float(self.per<=49):
          print("Pass Class")
        elif float(self.per>=0) and float(self.per<=39):
          print("Fail")
        else:
          print("Not Defined")
    def showData(self):
        print("Name of Student is:-",self.name)
        print("Enter the Number:-",self.number) 
        print("Marks of Maths:-",self.maths)
        print("Marks of English:-",self.english)
        print("Marks of Gujrati:-",self.gujrati)
        print("Total is:-",self.per)

s=Student()
name=input("Enter the name of Student:-")
number=int(input("Enter the Number of Student:-"))
maths=int(input("Enter the Marks of Maths:-"))
english=int(input("Enter the marks of English:-"))
gujrati=int(input("Enter the Marks of Gujrati:-"))
s.setData(name,number,maths,english,gujrati)
s.Calculation()
s.Grade()
s.showData()
