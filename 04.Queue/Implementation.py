from collections import deque

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        self.buffer.appendleft(data)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

if __name__ == '__main__':
    pq = Queue()
    pq.enqueue({
        'Company' : 'Wal Mart',
        'timestamp' : '20 Jan, 11.15 AM',
        'price' : 131.10
    })

    pq.enqueue({
        'Company': 'Wal Mart',
        'timestamp': '20 Jan, 11.16 AM',
        'price': 132
    })

    pq.enqueue({
        'Company': 'Wal Mart',
        'timestamp': '20 Jan, 11.17 AM',
        'price': 135
    })

    while not pq.is_empty():
        data = pq.dequeue()
        print(data)
