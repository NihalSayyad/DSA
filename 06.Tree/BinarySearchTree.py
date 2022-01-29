class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # Add this value in left sub tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # Add in right sub tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data

    def calc_sum(self):
        left_sum = self.left.calc_sum() if self.left else 0
        right_sum = self.right.calc_sum() if self.right else 0
        return self.data + left_sum + right_sum

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 21, 20, 9, 23, 18, 34]
    root = build_tree(numbers)
    print(root.in_order_traversal())

    print(root.search(20))
    print(root.find_min())
    print(root.find_max())
    print(root.calc_sum())