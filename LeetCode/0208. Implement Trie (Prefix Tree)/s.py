class Trie:
    def __init__(self):
        self.map = {'present':False}

    def insert(self, word: str) -> None:
        map = self.map # redefining keyword
        for letter in word:
            if not letter in map:
                map[letter] = {'present':False}
            map = map[letter]
        map['present'] = True


    def search(self, word: str) -> bool:
        map = self.map
        for letter in word:
            if letter in map:
                map = map[letter]
            else:
                return False
        return map['present']
        

    def startsWith(self, prefix: str) -> bool:
        map = self.map
        for letter in prefix:
            if letter in map:
                map = map[letter]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
