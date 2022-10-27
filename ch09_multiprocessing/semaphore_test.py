import multiprocessing
import time

restaurant = 5
s = multiprocessing.Semaphore(5)


def enter_restaurant(num):
    global restaurant
    print(f"Person {num} is waiting for his turn")
    s.acquire()
    print(f"Person {num} is enjoying his meal")

    time.sleep(2)

    s.release()
    print(f"Person {num} has left the restaurant")

if __name__ == "__main__":
    persons = []

    for i in range(20):
        persons.append(multiprocessing.Process(target=enter_restaurant, args=(i,)))
        persons[i].start()

    for i in range(20):
        persons[i].join()
