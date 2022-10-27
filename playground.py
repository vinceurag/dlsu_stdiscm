import multiprocessing

queue = multiprocessing.Queue()

print(queue.put("first"))
print(queue.put("second"))
print(queue.put("third"))

print(queue.get())
print(queue.get())
print(queue.get())
