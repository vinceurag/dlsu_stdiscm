import threading
import time
import random
import queue

queue = queue.Queue()
count = 10
consumer_threads = 2

class Producer(threading.Thread):
    def __init__(self, count):
        threading.Thread.__init__(self)
        self.counter = count

    def run(self):
        global queue
        time.sleep(3)
        print("Producer is waking up...")
        for i in range(self.counter):
            print(f"Producer appended an item: {i}")
            # put item into queue
            queue.put(i)
            time.sleep(random.randint(0,1))

class Consumer(threading.Thread):
    def __init__(self, count, thread_ID):
        threading.Thread.__init__(self)
        self.counter = int((count/consumer_threads))
        self.list = []
        self.item = 0
        self.ID = thread_ID

    def run(self):
        global queue
        print(f"Consumer {self.ID} is waiting...")
        for i in range(self.counter):
            self.item = queue.get()
            self.list.append(self.item)
            print(f"Consumer {self.ID} got an item {self.item}")
            time.sleep(random.randint(1,2))
        print(f"The values acquired by the consumer {str(self.ID)} are {str(self.list)}")

if __name__ == "__main__":
    c_threads_list = []
    for n in range(consumer_threads):
        c = Consumer(count=count, thread_ID=n)
        c_threads_list.append(c)
        c.start()

    p = Producer(count=count)
    p.start()

    for c in c_threads_list:
        c.join()

    p.join()
