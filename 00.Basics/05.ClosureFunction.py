def outerFunction(text):
    text = text

    def innerFunction():
        # Accessing outer variable
        print(text)

    return innerFunction

if __name__ == '__main__':
    myFunction = outerFunction('Hey!')
    myFunction()
    myFunction()
    myFunction()