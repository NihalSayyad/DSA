class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b


obj1 = Complex(1,2)
obj2 = Complex(2,3)
obj3 = obj1 + obj2
print(obj3)