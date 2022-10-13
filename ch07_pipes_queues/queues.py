import multiprocessing
from queue import Empty
import time

def initialize_images():
    images = []
    for i in range(100):
        images.append(f"image-{i}.jpg")

    return images

def enqueue_images(images, queue):
    for img in images:
        queue.put(img)
        print(f"{multiprocessing.current_process().name} - Enqueued image: {img}")

def adjust_brightness(queue):
    while not queue.empty():
        time.sleep(0.05)
        try:
            print(f"{multiprocessing.current_process().name} adjusted the brightness for image {queue.get(timeout=0.5)}")
        except Empty:
            print("Done!")

def run():
    images = initialize_images()

    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=enqueue_images, args=(images, queue))
    p2 = multiprocessing.Process(target=adjust_brightness, args=(queue,))
    p3 = multiprocessing.Process(target=adjust_brightness, args=(queue,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

if __name__ == "__main__":
    start_time = time.perf_counter()
    run()
    finish_time = time.perf_counter()
    print("Time elapsed:", round(finish_time - start_time), "seconds")
