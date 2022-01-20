from Implementation import Queue

def produce_binary_nums(n):
    numbers_queue = Queue()
    numbers_queue.enqueue('1')

    for i in range(n):
        front = numbers_queue.front()
        print(" ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()

if __name__ == '__main__':
    produce_binary_nums(10)