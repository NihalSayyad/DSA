from Implementation import Stack

def is_balanced(string):
    stack = Stack()

    for i in string:
        if i in ['[','{','(']:
            stack.push(i)
        else:
            if stack.is_empty():
                return False
            else:
                pop_val = stack.pop()
                if (i == "]" and pop_val == "[") or  (i == ")" and pop_val == "(") or (i=="}" and pop_val == "{"):
                    continue
                else:
                    return False

    return True

if __name__ == '__main__':
    string1 = "{[()]}"
    print(is_balanced(string1))