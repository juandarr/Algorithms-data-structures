class Node(object):
    def __init__(self, value=None, parentNode=None):
        self.value = value
        self.parentNode = parentNode
        self.children = {}
        self.isEnd = False

    def isLeaf(self):
        return len(self.children) == 0

    def addChild(self, value):
        self.children[value] = Node(value, self)


class Trie(object):
    def __init__(self, root=Node()):
        self.root = root
        self.wordCount = 0

    def isEmpty(self):
        return self.wordCount == 0

    def words(self):
        return self.wordsInSubtrie(self.root, "")

    # Insert a word in the trie
    def insert(self, word):
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

    # Finds whether a word is contained or not by the trie
    def contains(self, word, matchPrefix=False):
        if len(word) == 0:
            return False
        currentNode = self.root
        for character in word.lower():
            if character in currentNode.children:
                currentNode = currentNode.children[character]
            else:
                return False
        return matchPrefix or currentNode.isEnd

    def remove(self):
        pass

    # Finds array of words in a subtrie of a the trie
    def wordsInSubtrie(self, rootNode, partialWord):
        subtrieWords = []
        previousLetters = partialWord
        if rootNode.value is not None:
            previousLetters += rootNode.value
        if rootNode.isEnd:
            subtrieWords.append(previousLetters)
        for childNode in rootNode.children.values():
            childWords = self.wordsInSubtrie(childNode, previousLetters)
            subtrieWords.extend(childWords)
        return subtrieWords
