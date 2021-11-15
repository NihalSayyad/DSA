
def SortTheArray(arr):
    map = {}
    for i in arr:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    arr = []
    for i in range(3):
        if i in map:
            for k in range(map[i]):
                arr.append(i)

    return arr

if __name__ == '__main__':
    arr = [2,2,1,0,2,1,1,0,0]
    print(SortTheArray(arr))

