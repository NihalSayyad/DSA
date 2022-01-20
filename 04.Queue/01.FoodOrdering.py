from Implementation import Queue
import time
import threading

queue = Queue()

def place_order(orders):
    for food in orders:
        print("Placing : ", food)
        queue.enqueue(food)
        time.sleep(0.5)

def serve_order():
    while not queue.is_empty():
        food = queue.dequeue()
        print("Serving : ", food)
        time.sleep(2)

orders = ['pizza','samosa','pasta','biryani','burger']
t1 = threading.Thread(target=place_order, args=(orders,))
t2 = threading.Thread(target=serve_order)

t1.start()
time.sleep(1)
t2.start()

t1.join()
t2.join()

print("Done!")