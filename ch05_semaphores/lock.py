import threading
import time

counter = 0
shared_resource_lock = threading.Lock()

def increment(num):
    global shared_resource_lock
    print(threading.current_thread().name, 'is trying to acquire a lock')
    shared_resource_lock.acquire()
    print(threading.current_thread().name, 'acquired the lock')
    global counter

    local_counter = counter
    local_counter += num

    time.sleep(0.5)

    counter = local_counter
    print('Local counter: ', local_counter)
    shared_resource_lock.release()
    print(threading.current_thread().name, 'released the lock')

if __name__ == "__main__":
    p1 = threading.Thread(target=increment, args=(5,))
    p2 = threading.Thread(target=increment, args=(10,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print('Global counter: ', counter)
