class Node(object):
    """
    Node class

    Store main node properties and helper methods for the trie operations
    """
    def __init__(self, value=None, parentNode=None):
        """
        Constructor method

        Parameters
        ----------
        value : str
            Value stored in node
        parentNode: Node
            Parent Node, used in trie's delete operation
        children: dict(Node)
            Keeps track of children of current node
        isEnd: bool
            Indicates whether the node is an end node for a word
        """

        self.value = value
        self.parentNode = parentNode
        self.children = {}
        self.isEnd = False

    def isLeaf(self):
        """
        Checks whether the node is a leaf node or not

        Returns
        ----------
        boolean
            A boolean indicating whether the node is a leaf node or not
        """

        return len(self.children) == 0

    def addChild(self, value):
        """
        Adds child to the children dictionary of nodes
        """

        self.children[value] = Node(value, self)


class Trie(object):
    """
    Trie data structure for storage of hashable and associative data
    (e.g., english words, DNA sequences)

    Methods
    ----------
    isEmpty()
        Return whether trie is empty or not
    words()
        Returns an array of words stored in the trie
    insert(word)
        Insert word in trie
    contains(word, matchPrefix=False)
        Indicates whether a word is contained in the trie
    remove(word)
        Removed word from the trie
    """

    def __init__(self, root=Node()):
        """
        Constructor method

        Parameters
        ----------
            root: Node
                root node of Trie
            wordCount: int
                Counter of words stored in Trie
        """

        self.root = root
        self.wordCount = 0

    def isEmpty(self):
        """
        Checks whether the trie is empty or not

        Returns
        ----------
        boolean
            A boolean indicating whether the trie is empty or not
        """

        return self.wordCount == 0

    def words(self):
        """
        Traverses the trie searching for all the words stored in it

        Returns
        ----------
        list
            A list of words stored in the trie
        """

        return self._wordsInSubtrie(self.root, "")

    def insert(self, word):
        """
        Inserts a word in the trie
        """

        if len(word) == 0:
            return
        currentNode = self.root
        for character in word.lower():
            if character in currentNode.children:
                currentNode = currentNode.children[character]
            else:
                currentNode.addChild(character)
                currentNode = currentNode.children[character]
        if currentNode.isEnd:
            return
        self.wordCount += 1
        currentNode.isEnd = True

    def contains(self, word, matchPrefix=False):
        """
        Find whether a word is contained or not in the trie

        `matchPrefix` is used to require a match of the word as a prefix of
        another word in the trie or match only the entire word

        Returns
        ----------
        boolean
            A boolean indicating whether an entire or prefix word is present
            in the trie
        """

        if len(word) == 0:
            return False
        currentNode = self.root
        for character in word.lower():
            if character in currentNode.children:
                currentNode = currentNode.children[character]
            else:
                return False
        return matchPrefix or currentNode.isEnd

    def remove(self, word):
        """
        Removes word from the trie
        """

        if len(word) == 0:
            return
        terminalNode = self._findTerminalNodeOf(word)
        if not terminalNode:
            return
        if terminalNode.isLeaf():
            self._deleteNodesForWordEndingWith(terminalNode)
        else:
            terminalNode.isEnd = False
        self.wordCount -= 1

    def _findLastNodeOf(self, word):
        """
        Finds last node of word if defined in trie

        Returns
        ---------
        Node or None
            A node storing the last character of a word. Will return None
            when the entire word is not stored in trie
        """

        currentNode = self.root
        for character in word.lower():
            if character in currentNode.children:
                currentNode = currentNode.children[character]
            else:
                return None
        return currentNode

    def _findTerminalNodeOf(self, word):
        """
        Finds terminal node of word if defined in trie

        It uses the method `findLastNodeOf` as helper method

        Returns
        ----------
        Node or None
            A node storing the last character of a word. Will return None when
            the entire word is not store in trie
        """

        lastNode = self._findLastNodeOf(word)
        if lastNode:
            if lastNode.isEnd:
                return lastNode
        return None

    def _deleteNodesForWordEndingWith(self, terminalNode):
        """
        Deletes all nodes from a end node (for a word) upwards without breaking
        the storage of other words in trie
        """

        lastNode = terminalNode
        character = lastNode.value
        while lastNode.isLeaf():
            lastNode = lastNode.parentNode
            del lastNode.children[character]
            character = lastNode.value
            if lastNode.isEnd or lastNode.parentNode is None:
                break

    def _wordsInSubtrie(self, rootNode, partialWord):
        """
        Finds array of words in a subtrie given a rootNode and the partial
        word preceeding it

        Returns
        ----------
        list
            A list with all the words found from `rootNode` using `partialWord`
            as prefix
        """

        subtrieWords = []
        previousLetters = partialWord
        if rootNode.value is not None:
            previousLetters += rootNode.value
        if rootNode.isEnd:
            subtrieWords.append(previousLetters)
        for childNode in rootNode.children.values():
            childWords = self._wordsInSubtrie(childNode, previousLetters)
            subtrieWords.extend(childWords)
        return subtrieWords
