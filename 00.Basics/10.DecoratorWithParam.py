## Decorator with parameter

def decorator(*args, **kwargs):
    print("Inside Decorator")
    def inner(func):
        print("Inside inner function")
        print("I like", kwargs['key'])

        func()

    return inner

@decorator(key='GFG')
def my_func():
    print("Inside my_func")
