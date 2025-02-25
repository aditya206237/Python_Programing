import array as arr
a = arr.array('i', [12, 23, 99, 46, 57])
max=0
for i in range (0,5):
    if a[i]>max:
        max=a[i]

print("Maximum value of array is:-",max)