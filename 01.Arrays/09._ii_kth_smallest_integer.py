'''
Sorting approach.. TimSort(inbuild sort) -> O(n. log n)
                    No extra space required.
'''

def KthSmallest(arr, k):
    arr.sort()
    return arr[k-1]

if __name__ == '__main__':
    arr = [3, 14, 23, 11, 2, 7]
    k = 3
    print(KthSmallest(arr, k))