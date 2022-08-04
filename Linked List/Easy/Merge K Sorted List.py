# divide and conquer strategy:
class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.nxt:
            itr = itr.nxt

        itr.nxt = Node(data, None)

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
            itr = itr.nxt

        print(ll_str)


def merge_k_lists(lists):
    if not lists:
        return []
    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    l, r = merge_k_lists(lists[:mid]), merge_k_lists(lists[mid:])
    return merge_lists(l, r)


def merge_lists(left, right):
    dummy = Node(0, None)
    tail = dummy

    while True:
        if left is None:
            tail.nxt = right
            break
        if right is None:
            tail.nxt = left
            break

        if left.data <= right.data:
            tail.nxt = left
            left = left.nxt
        else:
            tail.nxt = right
            right = right.nxt
        tail = tail.nxt

    return dummy.nxt


"""list_a = LinkedList()
list_a.insert_values([10, 20, 30, 40, 50])
list_a.insert_values([20, 50, 1500, 2000, 7000])
list_a.insert_values([1, 2, 3, 4, 5])
lists = [[10, 20, 30, 40, 50], [20, 50, 1500, 2000, 7000], [1, 2, 3, 4, 5]]

list_a.print_ll()
list_a.head = merge_k_lists(lists)
list_a.print_ll()
"""


def merge(lists):
    mid = len(lists) // 2

    l, r = merge(lists[:mid]), merge(lists[mid:])
    return l, r


lists = [[16, 5, 4, 5], [100, 200, 50, 36], [12, 9, 2, 3, 4]]
print(merge(lists))

