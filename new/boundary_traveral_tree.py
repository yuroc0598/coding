#leetcode 545

# utilize preorder traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# separate the traversal into three steps, left boundary, leaves, right boundary, use recursive
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """ 
        leaves = []
        leftB = []
        rightB = []
        def printLeaves(root): 
            
            if(root): 
                printLeaves(root.left) 
                if root.left is None and root.right is None: 
                    leaves.append(root.val)
                printLeaves(root.right) 
        def printBoundaryLeft(root): 
            if(root): 
                if (root.left): 
                    leftB.append(root.val)
                    printBoundaryLeft(root.left) 
                elif(root.right): 
                    leftB.append(root.val)
                    printBoundaryLeft(root.right)
        def printBoundaryRight(root): 
            if(root): 
                if (root.right): 
                    printBoundaryRight(root.right) 
                    rightB.append(root.val)
                elif(root.left): 
                    printBoundaryRight(root.left) 
                    rightB.append(root.val)
        ans = []
        if (root): 
                ans.append(root.val)
                printBoundaryLeft(root.left) 
                ans = ans + leftB
                printLeaves(root.left) 
                
                printLeaves(root.right) 
                ans = ans + leaves
                printBoundaryRight(root.right)
                ans += rightB
        print leftB,leaves,rightB
        return ans
        
        
        
