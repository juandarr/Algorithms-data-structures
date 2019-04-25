class node:

    def __init__(self, value):
        self.value = value
        self.next = None

class linked_list:

    def __init__(self, head):
        self.head = head

    def insert(self, node):
        tmp_next = self.head
        self.head = node
        self.head.next = tmp_next


        