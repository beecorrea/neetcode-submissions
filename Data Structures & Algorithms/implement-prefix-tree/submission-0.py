class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            if curr.get_child(c) is None:
                curr.children[self.index(c)] = PrefixTree()
            curr = curr.get_child(c)
        
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self
        for c in word:
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
        