class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        self.root.insert(word)

    def search(self, word: str) -> bool:
        return self.root.search(word)

class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            if curr.get_child(c) is None:
                curr.children[self.index(c)] = Trie()
            curr = curr.get_child(c)
        
        curr.end_of_word = True
    
    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            c = word[i]

            if c == ".":
                for child in curr.children:
                    if child and child.search(word[i+1:]):
                        return True
                return False

            if curr.get_child(c) is None:
                return False
            curr = curr.get_child(c)

        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            if curr.get_child(c) is None:
                return False
            curr = curr.get_child(c)

        return True

    def index(self, char):
        return ord(char) - ord("a")
    
    def get_child(self, char):
        return self.children[self.index(char)]
        