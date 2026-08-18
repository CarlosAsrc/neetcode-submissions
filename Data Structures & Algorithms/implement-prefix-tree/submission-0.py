
class Node:
    def __init__(self):
        self.child = {}
        self.finishWorld = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.child:
                current.child[c] = Node()
            current = current.child[c]
        current.finishWorld = True



    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c not in current.child:
                return False
            current = current.child[c]
        return current.finishWorld
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.child:
                return False
            current = current.child[c]
        return True
        
        