def outerFunction(text):
    text = text

    def innerFunction():
        # Accessing outer variable
        print(text)

    innerFunction()

if __name__ == '__main__':
    outerFunction('Hey!')