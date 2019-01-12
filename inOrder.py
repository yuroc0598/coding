#!/usr/bin/env python
class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
# Iterative function for inorder tree traversal 
def inOrder(root): 
      
    # Set current to root of binary tree 
    
    if not root:
        return
    current = root  
    s = [] # initialze stack 
    done = 0 
      
    while not done: 
          
        # Reach the left most Node of the current Node 
        if current is not None: 
              
            # Place pointer to a tree node on the stack  
            # before traversing the node's left subtree 
            s.append(current) 
          
            current = current.left  
  
          
        # BackTrack from the empty subtree and visit the Node 
        # at the top of the stack; however, if the stack is  
        # empty you are done 
        else: 
            if s:
                current = s.pop() 
                print current.data, 
          
                # We have visited the node and its left  
                # subtree. Now, it's right subtree's turn 
                current = current.right  
            else:
                done = 1
  
  
# Driver program to test above function 
  
""" Constructed binary tree is 
            1 
          /   \ 
         2     3 
       /  \ 
      4    5   """
  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
inOrder(root) 
