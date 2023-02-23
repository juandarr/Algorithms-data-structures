# List sample to convert from list to linked list
ar = [1, 3, 5, 7, 0, 2, 10]


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


# Stores elements of list in array of nodes, initializes linked list with first
# element
nodes = []
start_node = Node(ar[0])
nodes.append(start_node)
ll = Linked_list(start_node)
for value in ar[1:]:
    new_node = Node(value)
    nodes[-1].next = new_node
    nodes.append(new_node)

# Traverse linked list
node = ll.first
while (node is not None):
    print(node.data)
    node = node.next
