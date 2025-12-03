class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True

    def _dfs(self, word: str, node: TrieNode) -> bool:
        for i in range(len(word)):
            if word[i] == ".":
                for childNode in node.children.values():
                    if i == len(word)-1:
                        if childNode.end:
                            return True
                    elif self._dfs(word[i+1:], childNode):
                        return True
                # no child works out
                return False
            elif word[i] not in node.children:
                return False
            else:
                node = node.children[word[i]]
        return node.end

    def search(self, word: str) -> bool:
        return self._dfs(word, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)