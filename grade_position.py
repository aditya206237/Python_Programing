per=float(input("Enter the Percentage obtained:-"))
if float(per>=80) and float(per<=100):
    print("Distinction")
elif float(per>=60) and float(per<=79):
    print("First Class")
elif float(per>=50) and float(per<=59):
    print("Second Class")
elif float(per>=40) and float(per<=49):
    print("Pass Class")
elif float(per>=0) and float(per<=39):
    print("Fail")
else:
    print("Not Defined")