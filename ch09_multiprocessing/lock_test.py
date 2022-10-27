import multiprocessing
import time

counter = 0
shared_resource_lock = multiprocessing.Lock()

def increment(num):
    global shared_resource_lock
    print(multiprocessing.current_process().name, 'is trying to acquire a lock')
    shared_resource_lock.acquire()
    print(multiprocessing.current_process().name, 'acquired the lock')
    global counter

    local_counter = counter
    local_counter += num

    time.sleep(0.5)

    counter = local_counter
    print('Local counter: ', local_counter)
    shared_resource_lock.release()
    print(multiprocessing.current_process().name, 'released the lock')

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=increment, args=(5,))
    p2 = multiprocessing.Process(target=increment, args=(10,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print('Global counter: ', counter)
