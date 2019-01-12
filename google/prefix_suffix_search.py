#leetcode 745
    
class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.weights = {}
        self.pre = collections.defaultdict(set)
        self.suf = collections.defaultdict(set)
        
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                self.pre[word[:j]].add(word)
                self.suf[word[j:]].add(word)
            self.weights[word] = i

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        weight = -1
        for word in self.pre[prefix] & self.suf[suffix]:
            if self.weights[word] > weight:
                weight = self.weights[word]
        return weight
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
