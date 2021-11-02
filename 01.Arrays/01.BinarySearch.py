

def binary_search(myList, target):
    left_index = 0
    right_index = len(myList) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = myList[mid_index]

        if mid_number == target:
            return mid_index

        if mid_number < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

def binary_search_recursive(myList, target, left_index, right_index):
    if left_index > right_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_number = myList[mid_index]

    if mid_number == target:
        return mid_index

    if mid_number < target:
        return binary_search_recursive(myList, target, mid_index+1, right_index)
    else:
        return binary_search_recursive(myList, target, left_index, mid_index-1)

if __name__ == '__main__':
    numbers = [2, 4, 7, 8, 10, 23, 27, 32, 33, 39, 42]
    target = 32
    print(f"Number found at index {binary_search_recursive(numbers, target, 0, len(numbers) - 1)}")