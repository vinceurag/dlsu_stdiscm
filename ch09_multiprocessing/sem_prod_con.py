import multiprocessing
import time
import random

count = 10

class Producer(multiprocessing.Process):
    def __init__(self, count, semaphore, buffer):
        multiprocessing.Process.__init__(self)
        self.counter = count
        self.semaphore = semaphore
        self.buffer = buffer

    def run(self):
        time.sleep(2)
        print("Producer is waking up...")
        for i in range(self.counter):
            self.buffer.append(i)
            self.semaphore.release()
            time.sleep(random.randint(0,1))
            print("Producer appended an item to the shared resource buffer")

class Consumer(multiprocessing.Process):
    def __init__(self, count, process_id, semaphore, buffer):
        multiprocessing.Process.__init__(self)
        self.counter = count
        self.list = []
        self.item = 0
        self.ID = process_id
        self.semaphore = semaphore
        self.buffer = buffer

    def run(self):
        print(f"Consumer {self.ID} is waiting for a sempahore...")
        for i in range(self.counter):
            self.semaphore.acquire()
            if self.buffer:
                self.item = self.buffer.pop()
                self.list.append(self.item)
                print(f"Consumer {self.ID} popped an item")

            time.sleep(random.randint(0,1))

        print(f"Data acquired by consumer: {self.list}")

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    shared_resource_buffer = manager.list()
    semaphore = multiprocessing.Semaphore(0)
    t1 = Consumer(count, 1, semaphore, shared_resource_buffer)
    t2 = Producer(count, semaphore, shared_resource_buffer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Shared resource buffer: {shared_resource_buffer}")
