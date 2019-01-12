#leetcode 211 add and search word, implement a trie, the word contain only letters and '.', which can represent any char


class TrieNode(object):
    def __init__(self):
        self.isEnd = False
        self.children = {}

class WordDictionary(object):


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        root = self.root
        for char in word:
            if char not in root.children:
                tmp = TrieNode()
                root.children[char]= tmp
            root = root.children[char]
        root.isEnd = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def helper(node,word):
            L = len(word)
            if L==0:
                return node.isEnd
            root = node
            for i in xrange(L):
                char = word[i]
                if char == '.':
                    for pos in root.children:
                        if helper(root.children[pos],word[i+1:]):
                            return True
                    return False
                if char not in root.children:
                    return False
                root = root.children[char]
            return root.isEnd
        return helper(self.root,word)

wd = WordDictionary()
wd.addWord('bad')
wd.addWord('dad')
wd.addWord('mad')
print wd.search('pad')
print wd.search('b.')
