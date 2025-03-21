n1=100
n2=0

try:
    ans=n1/n2 
    print("Ans is:-",ans)
except ZeroDivisionError as ex:
    print("ZeroDivisionError is:-",ex)
except ValueError as ex:
    print("ValueError is:-",ex)
except Exception as ex:
    print("Exception is:-",ex)
finally:
    print("This is finally block")    