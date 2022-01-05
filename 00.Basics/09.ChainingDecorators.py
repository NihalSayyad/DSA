## Chaining decorators means adding multiple decorators

def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1
@decor
def function():
    return 10

print(function())