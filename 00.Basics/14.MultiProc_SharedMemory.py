import multiprocessing

def calc_square(numbers, result):
    for idx, n in enumerate(numbers):
        result[idx] = n*n
    print("Inside process : ", result[:])

if __name__ == '__main__':
    numbers = [2,3,5,7]
    result = multiprocessing.Array('i', 4)
    p = multiprocessing.Process(target=calc_square, args=(numbers, result))

    p.start()
    p.join()

    print("outside : ", result[:])