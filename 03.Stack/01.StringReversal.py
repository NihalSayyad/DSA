from Implementation import Stack

line = "This is a line"
stack = Stack()
for i in range(len(line)):
    stack.push(line[i])

for i in range(len(line)):
    print(stack.pop(), end='')

