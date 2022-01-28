
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data):
        self.head = None
        for i in data:
            self.insert_at_end(i)

    def print_list(self):
        if self.head is None:
            print("List is empty")

        itr = self.head

        llstr = ''

        while itr:
            llstr += str(itr.data) + '---->'
            itr = itr.next
        print(llstr)

if __name__ == '__main__':

    ll.insert_values([1,2,3,4,5])
    ll.print_list()