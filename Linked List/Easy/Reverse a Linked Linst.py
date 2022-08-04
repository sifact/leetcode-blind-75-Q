class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
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

    def reverse_list(self):
        prev = None

        head = self.head

        while head:
            curr = head
            head = head.next
            curr.nxt = prev
            prev = curr

        self.head = prev
        self.print()

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def print(self):
        if self.head is None:
            print("Linked list is blank")
            return

        itr = self.head
        linked_list = ''

        while itr:
            linked_list += str(itr.data) + '>--'
            itr = itr.nxt

        print(linked_list)


ll = LinkedList()
ll.insert_values([1, 2, 3])
ll.reverse_list()







