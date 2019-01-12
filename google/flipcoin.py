#!/usr/bin/python3

import time
import random
def flipc(nums):
    dp = {}
    L = len(nums)
    def helper(start,end):
        if (start,end) not in dp:    
            if end - start == 1:
                dp[(start,end)] = max(nums[start],nums[end])
            else:

                p1=nums[start]+helper(start+2,end)
                p2=nums[start]+helper(start+1,end-1)
                v1 = min(p1,p2)


                p3=nums[end]+helper(start+1,end-1)
                p4=nums[end]+helper(start,end-2)
                v2 = min(p3,p4)
                dp[(start,end)] = max(v1,v2)
        return dp[(start,end)]
    return helper(0,L-1)

def op(arr): 
    n = len(arr)  
    # Create a table to store  
    # solutions of subproblems  
    table = [[0 for i in range(n)] 
                for i in range(n)] 
  
    # Fill table using above recursive  
    # formula. Note that the table is  
    # filled in diagonal fashion  
    # (similar to http:// goo.gl/PQqoS), 
    # from diagonal elements to 
    # table[0][n-1] which is the result.  
    for gap in range(n): 
        for j in range(gap, n): 
            i = j - gap 
              
            # Here x is value of F(i+2, j),  
            # y is F(i+1, j-1) and z is  
            # F(i, j-2) in above recursive  
            # formula  
            x = 0
            if((i + 2) <= j): 
                x = table[i + 2][j] 
            y = 0
            if((i + 1) <= (j - 1)): 
                y = table[i + 1][j - 1] 
            z = 0
            if(i <= (j - 2)): 
                z = table[i][j - 2] 
            table[i][j] = max(arr[i] + min(x, y), 
                              arr[j] + min(y, z)) 
    return table[0][n - 1] 

nums = []
for _ in range(1000):
    nums.append(random.randint(0,1000))
t1 = time.time()
print(flipc(nums))
t2 = time.time()
print(op(nums))
t3 = time.time()

print("two time :{}, {}".format(t2-t1,t3-t2))

