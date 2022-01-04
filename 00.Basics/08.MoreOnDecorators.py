def hello_decorator(func):

    def inner1(*args, **kwargs):
        print("Before execution")

        returned_value = func(*args, **kwargs)
        print("After execution")

        return returned_value

    return inner1


@hello_decorator
def sum_of_numbers(a, b):
    print("From actual function")
    return a + b

print("sum = ", sum_of_numbers(10, 20))