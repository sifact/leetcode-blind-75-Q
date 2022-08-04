class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def print_ll(self):
        if self.head is None:
            print("Linked List is empty node!")

        itr = self.head
        ll_str = ""
        while itr:
            ll_str += str(itr.data) + ' ' + '>-' + ' '
            itr = itr.next

        print(ll_str)


def merge_lists(head_a, head_b):
    dummy = Node(0, None)
    tail = dummy

    while True:
        if head_a is None:
            tail.next = head_b
            break
        if head_b is None:
            tail.next = head_a
            break

        if head_a.data <= head_b.data:
            tail.next = head_a
            head_a = head_a.next
        else:
            tail.next = head_b
            head_b = head_b.next

        tail = tail.next

    return dummy.next


list_a = LinkedList()
list_a.insert_values([20, 50, 1500, 2000, 7000])
list_a.print_ll()

list_b = LinkedList()
list_b.insert_values([10, 300, 1000, 1200, 1400])
list_b.print_ll()

list_a.head = merge_lists(list_a.head, list_b.head)
list_a.print_ll()
