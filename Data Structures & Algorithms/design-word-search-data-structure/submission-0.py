
class Node:
    def __init__(self):
        self.c = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.c:
                current.c[c] = Node()
            current = current.c[c]
        current.isWord = True
        

    def search(self, word: str) -> bool:
        
        def searchAll(word, current):
            for i, c in enumerate(word):
                if c != '.' and c not in current.c:
                    return False
                if c == '.':
                    b = False
                    for j, v in current.c.items():
                        b = b or searchAll(word[i+1:], v)
                    return b
                current = current.c[c]
            return current.isWord

        return searchAll(word, self.root)
        
