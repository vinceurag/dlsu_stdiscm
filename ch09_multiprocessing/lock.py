import multiprocessing
import time

def increment(lock, counter, num):
    print(multiprocessing.current_process().name, 'is trying to acquire a lock')
    lock.acquire()
    print(multiprocessing.current_process().name, 'acquired the lock')

    counter.value = counter.value + num

    time.sleep(0.5)

    print('Local counter: ', counter.value)
    lock.release()
    print(multiprocessing.current_process().name, 'released the lock')

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    shared_counter = manager.Value('i', 0)
    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=increment, args=(lock, shared_counter, 5,))
    p2 = multiprocessing.Process(target=increment, args=(lock, shared_counter, 10,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print('Global counter: ', shared_counter.value)
