from threading import Thread
import time
def factorial_and_sum(no):
    fact = 1
    sum = 0
    while no <= 10:
        fact=fact*no
        sum=sum+no
        print("Number:" ,no, "Factorial:", fact, "Sum:", sum)
        time.sleep(1)
        no=no+1

Thread(target=factorial_and_sum, args=(1,)).start()