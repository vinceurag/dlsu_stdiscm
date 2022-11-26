import threading
import time

shared_resource_without_lock=0
COUNT=100

##No lock management##
def increment_without_lock():
    global shared_resource_without_lock

    for i in range (COUNT):
        shared_resource_without_lock +=1
        time.sleep(0.05)

def decrement_without_lock():
  global shared_resource_without_lock

  for i in range (COUNT):
    shared_resource_without_lock -=1

##Main program
if __name__=="__main__":
    t1 = threading.Thread(target=increment_without_lock)
    t2 = threading.Thread(target=decrement_without_lock)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print ("The value of shared variable with race condition is %s" %shared_resource_without_lock)
