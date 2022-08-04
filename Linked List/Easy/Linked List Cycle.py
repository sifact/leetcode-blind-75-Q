# floyd cycle detection algorithm:
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def has_cycle(self):
        if not self.head:
            return False

        slow = self.head
        fast = self.head.nxt

        while slow != fast:
            if not fast or not fast.nxt:
                return False
            slow = slow.nxt
            fast = fast.nxt.nxt

        return True

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


ll = LinkedList()
ll.insert_values([1, 2, 3, 2])
print(ll.has_cycle())


