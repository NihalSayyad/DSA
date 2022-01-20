import time

def calc_square(numbers):
    print("Calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print("square  : ", n*n)

def calc_cube(numbers):
    print("Calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("cube : ", n*n*n)

arr = [2,3,4,8,9]
t=time.time()
calc_square(arr)
calc_cube(arr)

print("Done with all the task in ", time.time() - t)