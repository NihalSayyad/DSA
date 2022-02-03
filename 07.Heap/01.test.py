class Heap:
    def __init__(self):
        self.arr = []

    def heapify(self):
        size = len(self.arr)
        for i in range(size-1, -1, -1):
            largest = i
            l = i*2 + 1
            r = i*2 + 2

            if l < size and self.arr[l] > self.arr[i]:
                largest = l

            if r < size and self.arr[r] > self.arr[largest]:
                largest = r

            if largest != i:
                self.arr[largest], self.arr[i] = self.arr[i], self.arr[largest]
                self.heapify()


    def insert(self, data):
        size = len(self.arr)
        if size == 0:
            self.arr.append(data)
        else:
            self.arr.append(data)
            self.heapify()

    def print_heap(self):
        print(self.arr)

if __name__ == '__main__':
    arr = [4,3,5,7,2,9,10]
    heap = Heap()
    for i in arr:
        heap.insert(i)

    heap.print_heap()
    heap.insert(22)
    heap.print_heap()