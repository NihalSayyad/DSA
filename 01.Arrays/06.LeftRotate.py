# Left rotate array by 1 position

def left_rotate_by_one(arr):
    len_arr = len(arr)
    if len_arr <= 1:
        return

    first_element = arr[0]
    for i in range(1, len_arr):
        arr[i - 1] = arr[i]

    arr[len_arr - 1] = first_element


if __name__ == '__main__':
    arr = [ 1,2,3,4,5,6,7,8,9,10]
    left_rotate_by_one(arr)
    print(arr)