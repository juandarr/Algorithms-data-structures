class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def is_last(self):
        return self.next is None

class Linked_list(object):
    def __init__(self, first=None):
        self.first = first

    def is_empty(self):
        return self.first is None