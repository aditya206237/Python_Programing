from threading import Thread
import time
def fat_torial(no):
    fact=1
    while no<=10:
     fact=fact*no
     print("Factorial of",no,"is:-",fact)
     time.sleep(1)
     no=no+1
Thread(target=fat_torial,args=(1,)).start()