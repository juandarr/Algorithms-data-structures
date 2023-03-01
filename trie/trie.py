class Node(object):
    def __init__(self, value=None, parentNode=None):
        self.value = value
        self.parentNode = parentNode
        self.children = {}
        self.isEnd = False


class Trie(object):
    def __init__(self, root=Node()):
        self.root = root

    # Define trie operations here
    def insert(self):
        pass

    def contains(self):
        pass

    def remove(self):
        pass

    def wordInSubtrie(self):
        pass
