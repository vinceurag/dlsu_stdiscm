import threading
import time

s = threading.Semaphore()
counter = 0

def increment(num):
    print(threading.currentThread().name, 'is trying to acquire a semaphore')
    s.acquire()
    print(threading.currentThread().name, 'acquired the semaphore')
    global counter

    local_counter = counter
    local_counter += num

    time.sleep(0.5)

    counter = local_counter
    print('Local counter: ', local_counter)
    s.release()
    print(threading.currentThread().name, 'released the semaphore')

t1 = threading.Thread(target=increment, args=(5,))
t2 = threading.Thread(target=increment, args=(10,))

t1.start()
t2.start()

t1.join()
t2.join()

print('Global counter: ', counter)