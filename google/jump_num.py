#!/usr/bin/python3

def jmp_num(n):
    dd = {0:[1],1:[0,2],2:[1,3],3:[2,4],4:[3,5],5:[4,6],6:[5,7],7:[6,8],8:[7,9],9:[8]}
    ans = []
    for i in range(min(n,10)):
        ans.append(i)
    for i in range(1,10):
        print("i is %d\n"%i)
        arr = [i]
        while arr:
            for exist in arr:
                tmp = []
                print("ans is {}".format(ans))
                for cur in dd[exist%10]:
                    new = exist*10+cur
                    if new<n:
                        ans.append(new)
                        tmp.append(new)
                arr = tmp
                print("arr is {}".format(arr))
    return ans
        

print(jmp_num(105))
