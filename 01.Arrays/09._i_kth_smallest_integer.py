'''
MinHeap approach.. complexity O(n.log n)
                    extra space to store the mean heap O(n)
'''

from heapq import heappush, heappop, heapify

def KthSmallest(arr, k):
    heap = []
    heapify(heap)

    for i in arr:
        heappush(heap, i)

    count = 0
    for i in range(k-1):
        heappop(heap)

    return heappop(heap)


if __name__ == '__main__':
    arr = [3, 14, 23, 11, 2, 7]
    k = 3
    print(KthSmallest(arr, k))