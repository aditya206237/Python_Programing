import array as arr
a = arr.array('i', [12, 23, 99, 46, 57])
temp=1
for i in range(0,5):
    for j in range (i):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
for i in range (0,5):
    print(a[i])