import threading
import time

event = threading.Event()

def greet():
    time.sleep(3)
    print("Hello, my name is Jeff.")
    event.set()

def answer():
    event.wait()
    print("Hello Jeff!")

t1 = threading.Thread(target=greet)
t2 = threading.Thread(target=answer)

t1.start()
t2.start()

t1.join()
t2.join()
