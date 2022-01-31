
class Heap:
    def __init__(self):
        self.arr = []

    def heapify(self, n, i):
        largest = i
        left = (2 * i) + 1
        right = (2 * i) + 2

        if left < n and self.arr[i] < self.arr[left]:
            largest = left

        if right < n and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(n, largest)

    def insert(self, data):
        size = len(self.arr)
        if size == 0:
            self.arr.append(data)
        else:
            self.arr.append(data)
            for i in range((size // 2) - 1, -1, -1):
                self.heapify(size, i)

    def print_heap(self):
        print(self.arr)


if __name__ == '__main__':
    heap = Heap()
    heap.insert(23)
    heap.insert(10)
    heap.insert(29)
    heap.insert(12)
    heap.print_heap()
