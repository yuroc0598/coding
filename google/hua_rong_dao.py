# similar to LC 773, sliding puzzle, cao cao bai zou hua rong dao
from collections import deque
def hrd(board): # board in matrix format, convert to string?
    initB = ''
    initInd = 0
    for i in xrange(3):
        for j in xrange(3):
            char = str(board[i][j])
            initB += char
            if char == '0':
                initInd = 3*i+j
    nex = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4,6],4:[1,3,5,7],5:[2,4,8],6:[3,7],7:[4,6,8],8:[5,7]}
    Q = []
    step = 0
    seen = set()
    Q.append([initB,initInd])
    while Q:
        newQ = []
        for curB,curInd in Q:
            if curB == '123456780':
                return step
            seen.add(curB)
            for newInd in nex[curInd]:
                oldlist = list(curB)
                oldlist[curInd],oldlist[newInd] = oldlist[newInd],oldlist[curInd]
                newB = ''.join(oldlist)
                if newB not in seen:
                    newQ.append([newB,newInd])
        Q = newQ
        step += 1
    return -1

board = [[8,0,2],[1,4,6],[7,5,3]]
print hrd(board)
        
