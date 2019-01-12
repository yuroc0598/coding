# given N*N matrix with number 1 to N*N, find the max sequence, can only go horizontally or vertically

def max_seq(mat):
    if not mat or not mat[0]:
        return []
    N = len(mat)
    ans = 0
    def helper(i,j,visited,start,end):
        curL = end-start+1
        if (i,j) in visited:
            return curL
        if i<0 or i>N-1 or j<0 or j>N-1:
            return curL
        if mat[i][j] != end+1:
            return curL
        visited.add((i,j))
        curL += 1
        for newi,newj in [[i-1,j],[i+1,j],[i,j+1],[i,j-1]]:
            curL = max(curL,helper(newi,newj,visited,start,end+1))
        return curL       
    for i in xrange(N):
        for j in xrange(N):
            visited = set()
            ans = max(ans,helper(i,j,visited,mat[i][j],mat[i][j]-1))
    return ans
       
mat = [[3,2,5],[4,1,6],[9,8,7]]
print max_seq(mat)
