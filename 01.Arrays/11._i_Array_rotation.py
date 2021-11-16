'''
https://www.geeksforgeeks.org/array-rotation/
Extra space will be required to store the d elements.
Time Complexity --> O(n)
'''

def ArrayRotation(arr, d):
    temp = []
    for i in range(d):
        temp.append(arr[i])

    for i in temp:
        arr.remove(i)
        arr.append(i)

    return arr



if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    d = 3
    print(ArrayRotation(arr, d))