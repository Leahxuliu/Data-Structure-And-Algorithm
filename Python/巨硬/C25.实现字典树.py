'''
208 实现字典树
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
        curr.is_word = True
        return 

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


a = Trie()
a.insert('apple')
print(a.search('app'))
print(a.startsWith('app'))
print(a.search('apple'))

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)class TrieNode:


'''
211
"b.." 
'''
class Trienode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trienode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trienode()
            curr = curr.children[char]
        curr.is_word = True
        return 

    def search(self, word: str) -> bool:
        return self.find(word, 0, self.root)
        
    def find(self, word, start, root):
        if start == len(word):
            return root.is_word

        if word[start] == '.':
            for curr in root.children:
                # 易错！curr不是node，是key！root.children[curr]才是node
                if self.find(word, start + 1, root.children[curr]) == True:
                    return True
            return False

        else:
            if word[start] not in root.children:
                return False
            return self.find(word, start + 1, root.children[word[start]])



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)