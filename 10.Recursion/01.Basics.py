
def func(x, n):
    if n == 0:
        return 1
    elif n%2 == 0:
        return func(x*x, n//2)
    else:
        return x * func(x*x, (n-1)//2)

print(func(2,10))