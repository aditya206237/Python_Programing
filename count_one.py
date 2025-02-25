counts=0
for i in range (101):
    num=i
    while num>0:
        if num % 10 ==1:
            counts =counts +1
        num=num//10
print("Number of 1 in between 1 to 100 is:-",counts)
