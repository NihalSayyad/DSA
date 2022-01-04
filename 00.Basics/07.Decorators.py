
#defining a decorator
def hello_decorator(func):

    ## inner_1 is a wraper function in which argument i.e. func is called
    def inner_1():
        print("This is before function execution")

        func()

        print("This is after function execution")

    return inner_1

def actual_function():
    print("This is actual function")

actual_function = hello_decorator(actual_function)

actual_function()