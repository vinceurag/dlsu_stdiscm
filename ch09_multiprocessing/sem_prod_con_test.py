import multiprocessing
import time
import random

shared_resource_buffer = []
semaphore = multiprocessing.Semaphore(0)
count = 10

class Producer(multiprocessing.Process):
    def __init__(self, count):
        multiprocessing.Process.__init__(self)
        self.counter = count

    def run(self):
        global shared_resource_buffer
        global semaphore

        time.sleep(2)
        print("Producer is waking up...")
        for i in range(self.counter):
            shared_resource_buffer.append(i)
            semaphore.release()
            time.sleep(random.randint(0,1))
            print("Producer appended an item to the shared resource buffer")

class Consumer(multiprocessing.Process):
    def __init__(self, count, process_id):
        multiprocessing.Process.__init__(self)
        self.counter = count
        self.list = []
        self.item = 0
        self.ID = process_id

    def run(self):
        global shared_resource_buffer
        global semaphore

        print(f"Consumer {self.ID} is waiting for a sempahore...")
        for i in range(self.counter):
            semaphore.acquire()
            if shared_resource_buffer:
                self.item = shared_resource_buffer.pop()
                self.list.append(self.item)
                print(f"Consumer {self.ID} popped an item")

            time.sleep(random.randint(0,1))

        print(f"Data acquired by consumer: {self.list}")

if __name__ == "__main__":
    t1 = Consumer(count, 1)
    t2 = Producer(count)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Shared resource buffer: {shared_resource_buffer}")
