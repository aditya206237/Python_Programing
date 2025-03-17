from threading import Thread
import time
def sum_numbers(no):
    sum = 0
    while no<=10:
        sum=sum+no
        print(no,"sum is:-",sum)
        time.sleep(1)
        no=no+1
def fact_numbers(no):
    fact=1
    while no<=10:
        fact=fact*no
        print(no,"Fact is:-",fact)
        time.sleep(1)
        no=no+1
Thread(target=sum_numbers,args=(1,)).start()
Thread(target=fact_numbers,args=(1,)).start()