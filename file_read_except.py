
try:
    f=open("aditya.txt","r")
    print("Data from file")
    print(f.read())
    f.close()
except Exception as e:
    print("Exception is:-",e)
finally:
    print("This is finally block")