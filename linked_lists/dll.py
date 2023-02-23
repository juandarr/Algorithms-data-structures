# List sample to convert from list to linked list
ar = [1, 3, 5, 7, 0, 2, 10]


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


# Stores elements of list in array of nodes, initializes linked list with first
# element
nodes = []
start_node = Node(ar[0])
nodes.append(start_node)
ll = Double_linked_list(start_node)
for value in ar[1:]:
    new_node = Node(value)
    new_node.prev = nodes[-1]
    nodes[-1].next = new_node
    nodes.append(new_node)
ll.last = nodes[-1]


# Traverse double linked list forward
node = ll.first
print('Traversing forward')
while (node is not None):
    print(node.data)
    node = node.next


# Traverse double linked list backward
node = ll.last
print('\nTraversing backward')
while (node is not None):
    print(node.data)
    node = node.prev
