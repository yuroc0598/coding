# find the closest 1,2 pair in nums

def dist12(nums):
    p1 = p2 = float('-inf')
    ans = float('inf')
    for i in xrange(len(nums)):
        if nums[i] not in [1,2]:
            continue
        if nums[i]==1:
            p1 = i
        elif nums[i] == 2:
            p2 = i
        ans = min(abs(p2-p1),ans)
        if ans == 1: return 1
    return ans


def dist12_mat(mat):
    row,col = len(mat),len(mat[0])
    ans = [float('inf')]
    def helper(m,n,seek,visited):
        stack = [[m,n]]
        dist = 0
        while stack:
            if dist >= ans[0]: 
                return 
            tmp = []
            while stack:
                i,j = stack.pop()
                if (i,j) in visited:
                    continue
                if i<0 or i>=row or j<0 or j>=col:
                    continue
                visited.add((i,j))
                if mat[i][j] == seek:
                    ans[0] = dist
                    return
                for newi,newj in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]:
                    tmp.append([newi,newj])
            stack = tmp
            dist += 1
        return 

    for i in xrange(row):
        for j in xrange(col):
            if mat[i][j] not in [1,2]:
                continue
            visited = set()
            helper(i,j,3-mat[i][j],visited)
            if ans[0] == 1: return 1
    return ans[0]
        
nums = [1,5,9,7,3,2,4,3,1,4,56,2,3,4,5,2]
print dist12(nums)
mat = [[2,2,8,1],[2,5,6,3],[5,0,4,6]]
print dist12_mat(mat)
