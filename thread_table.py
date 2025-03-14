from threading import Thread
def multiply_numbers(x):
    for i in range (0,10):
        i=i+1
        result = x * i
        print('{} * {} = {}'.format(x, i, result))

Thread(target = multiply_numbers,args = (2,)).start()
