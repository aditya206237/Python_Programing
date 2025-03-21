n1=100
n2=0

try:
    ans=n1/n2
    print("Ans is:-",ans)
except Exception as e:
    print("Exception is:-",e)
finally:
    print("This is finally block")