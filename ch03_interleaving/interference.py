import threading
import time

greetings = "Hello, "

def greet(name):
    global greetings
    greetings_in_thread = greetings + name
    time.sleep(0.05)
    greetings = greetings_in_thread

t1 = threading.Thread(target=greet, args=["Adrian"])
t2 = threading.Thread(target=greet, args=["Rinzai"])

t1.start()
t2.start()

t1.join()
t2.join()

print(greetings)