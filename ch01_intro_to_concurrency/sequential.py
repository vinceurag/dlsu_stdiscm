import time

start_time = time.perf_counter()

patient_names = ["Aaron", "RJ", "Justin", "Darv", "Nics"]

def vaccinate(name):
    print("Vaccinated", name, "| Now monitoring")
    time.sleep(3)
    print(name, "was sent home.")

for patient_name in patient_names:
    vaccinate(patient_name)

finish_time = time.perf_counter()

print("Time elapsed:", round(finish_time - start_time), "seconds")