class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def is_last(self):
        return self.next is None

    def is_first(self):
        return self.prev is None


class Double_linked_list(object):
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last

    def is_empty(self):
        return self.first is None