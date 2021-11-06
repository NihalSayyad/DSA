#Partition

def partition(low, high, arr):
    pivot = arr[low] #Selecting first element as pivot can lead to O(n^2)
    i = low
    j = high
    while i < j:
        while True:
            i += 1
            if arr[i] > pivot:
                break
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

#Quick sort
def quick_sort(low, high, arr):
    if low < high:
        j = partition(low, high, arr)
        quick_sort(low, j, arr)
        quick_sort(j+1, high, arr)


if __name__ == '__main__':
    arr = [5,3,4,1,6,7,9,10]
    quick_sort(0, len(arr)-1, arr)
    print(arr)