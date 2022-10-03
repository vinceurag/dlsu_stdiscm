import threading
import time

restaurant = 5

def enter_restaurant(num):
    global restaurant
    print(f"Person {num} is waiting for his turn")
    print(f"Person {num} is enjoying his meal")
    time.sleep(2)

    print(f"Person {num} has left the restaurant")

persons = []

for i in range(20):
    persons.append(threading.Thread(target=enter_restaurant, args=(i,)))
    persons[i].start()

for i in range(20):
    persons[i].join()