#!/usr/bin/python3

#def knapsack(W,val,wt): # different from classical bag problem, this one requires the weight to be exact




def knapsack1(W,val,wt,n):
    def helper(W,val,wt,n):
        if W==0 or n==0:
            return 0
        if wt[n-1]>W:
            return helper(W,val,wt,n-1)
        return max(helper(W,val,wt,n-1),helper(W-wt[n-1],val,wt,n-1)+val[n-1])

    return helper(W,val,wt,n)

def knapsack2(W,val,wt,n):
    dp = [[0 for _ in range(n+1)] for _ in range(W+1)]
    for i in range(W+1):
        if i == 0:
            continue
        for j in range(n+1):
            if j == 0:
                continue
            if wt[j-1]>W:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-wt[j-1]][j-1]+val[j-1])
    return dp[W][n]

def knapsack3(W,val,wt,n):
    dp = [0 for _ in range(W+1)]
    for k in range(1,W+1):
        pos = [dp[k-wt[i]]+val[i] for i in range(n) if wt[i]<=k]
        print("k is {} and possible is {}".format(k,pos))
        if pos:
            dp[k] = max(pos)
    return dp[W]


W=50
wt=[10,20,30]
val=[60,100,120]
n=3

W=100
val=[1,30]
wt=[1,50]
n=2
print(knapsack3(W,val,wt,n))
