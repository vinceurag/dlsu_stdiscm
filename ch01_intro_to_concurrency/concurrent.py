import time
import threading

start_time = time.perf_counter()

patient_names = ["Aaron", "RJ", "Justin", "Darv", "Nics"]
threads = []

def vaccinate(name):
    print(threading.current_thread())
    print("Vaccinated", name, "| Now monitoring")
    time.sleep(3)
    print(threading.current_thread())
    print(name, "was sent home.")

for patient_name in patient_names:
    t = threading.Thread(target=vaccinate, args=[patient_name])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish_time = time.perf_counter()
print(threading.current_thread())
print("Time elapsed:", round(finish_time - start_time), "seconds")