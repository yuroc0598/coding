class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        def nb(r,c):
            anb = [[r-1,c-2],[r+1,c-2],[r+1,c+2],[r-1,c+2],[r-2,c-1],[r+2,c+1],[r-2,c+1],[r+2,c-1]]
            ans = []
            for item in anb:
                if -1<item[0]<N and -1<item[1]<N:
                    ans.append(item)
            return ans
        self.dp_pp = {}
        self.dp_nb = {}
        for i in xrange(N):
            for j in xrange(N):
                self.dp_pp[(i,j,0)]=1

        if not -1<r<N or not -1<c<N:
            return 0
        if K==0:
            return 1
        if (r,c,K) in self.dp_pp:
            print "found history"
            return self.dp_pp[(r,c,k)]
        if (r,c) not in self.dp_nb:
            self.dp_nb[(r,c)] = nb(r,c)
            
        ls,ans = len(self.dp_nb[(r,c)]),0
        if ls == 0:
            return 0
        curP = ls/float(8)
        if K == 1:
            return curP
        #print "K:{},current pos:{},current pb:{},next stack:{}".format(K,[r,c],curP,stack)
        # determine the propability of remain in this round, push all possible next pos in the stack
        for newr,newc in self.dp_nb[(r,c)]:
            ans += self.knightProbability(N,K-1,newr,newc)
        self.dp_pp[r,c,K] = curP*ans/ls
        return curP*ans/ls

s=Solution()
print s.knightProbability(8,9,6,4)
