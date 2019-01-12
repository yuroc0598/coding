import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        
        left = set()
        right = set()
        left.add(beginWord)
        right.add(endWord)
        if beginWord in wordList:
            wordList.remove(beginWord)
        wordList.remove(endWord)
        dd = set(wordList)
        step = 1
        while left and right:
            if len(left)>len(right) :
                left,right = right,left   
            newset = set()
            for ele in left:
                for i in range(len(ele)):
                    front = ele[:i]
                    back = ele[i+1:]
                    for char in string.ascii_lowercase:
                        mutate = front+char+back
                        if mutate in right:
                            return step+1
                        if mutate in dd:
                            dd.remove(mutate)
                            newset.add(mutate)
            left = newset
            step += 1
        return 0
def main():
    s = Solution()

    be='hit'
    en='cog'
    wordList=["hot","dot","dog","lot","log","cog"]
    print s.ladderLength(be,en,wordList)


if __name__ == '__main__':
    main()
