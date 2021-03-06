
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

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def inser_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next

        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange",])
    ll.print_list()

    ll.inser_at(0, "figs")
    ll.print_list()

    ll.inser_at(2,"jackfruit")
    ll.print_list()

    ll.insert_after_value("mango", "apple")
    ll.print_list()

    ll.insert_after_value("orange", "pears")
    ll.print_list()

    ll.remove_by_value("banana")
    ll.print_list()

    ll.remove_by_value("pears")
    ll.print_list()