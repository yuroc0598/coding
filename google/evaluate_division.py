# LC 399

from collections import defaultdict,deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
    
        cmap = defaultdict(set)
        L = len(equations)
        for i in xrange(L):
            p,c = equations[i]
            weight = values[i]
            cmap[p].add((c,weight))
            cmap[c].add((p,1/float(weight)))
        
        def check(p,c):
            
            if p not in cmap:
                return -1
            if p==c: return 1
            Q = deque()
            Q.append((p,1))
            seen = set()
            while Q:
                curnode,curw = Q.popleft()
                for nexnode,nexw in cmap[curnode]:
                    if nexnode == c:
                        cmap[p].add((c,curw*nexw))
                        cmap[c].add((p,1/float(curw*nexw)))
                        #print cmap
                        return curw*nexw
                    if (curnode,nexnode) not in seen:
                        Q.append((nexnode,curw*nexw))
                        seen.add((curnode,nexnode))
            return -1
        ans = []
        for p,c in queries:
            ans.append(check(p,c))
        return ans
