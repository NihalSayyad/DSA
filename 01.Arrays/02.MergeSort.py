#Merge Sort

def merge_two_sorted_arrays(a, b):
    n = len(a)
    m = len(b)
    i = j = 0
    c =[]
    while i<n and j< m:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < n:
        c.append(a[i])
        i += 1
    while j < m:
        c.append(b[j])
        j += 1
    return c

if __name__ == '__main__':
    a = [5,8,12,56]
    b = [7,9,45,51]

    print(merge_two_sorted_arrays(a,b))