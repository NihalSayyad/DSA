import multiprocessing
import time

def place_order(orders, queue):
    for food in orders:
        print("Placing : ", food)
        queue.put(food)
        time.sleep(0.5)

def serve_order(queue):
    while not queue.empty():
        food = queue.get()
        print("Serving : ", food)
        time.sleep(2)

if __name__ == '__main__':
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=place_order, args=(orders,queue))
    p2 = multiprocessing.Process(target=serve_order, args=(queue,))

    p1.start()
    time.sleep(1)
    p2.start()

    p1.join()
    p2.join()

    print("Done!")