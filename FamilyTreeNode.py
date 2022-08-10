class BinaryTreeNode:
    def __init__(self, root):
        self.root = root
        self.children = []
        self.siblings = []
        self.father = None
        self.mother = None

    def getRoot(self):
        return self.root

    def getChildren(self):
        return self.children

    def getSiblings(self):
        return self.siblings

    def getFather(self):
        return self.father

    def getMother(self):
        return self.mother

    def getNElement(self, n):
        if n >= 0 and n < len(self.children):
            return self.children[n]
        else:
            return self.children

