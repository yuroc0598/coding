#!/usr/bin/python3





def flood_fill(mat,x,y,new_color):
    print(mat)
    row,col = len(mat),len(mat[0])
    old_color = mat[x][y] 
    def dfs(x,y):
        if(x<0 or y<0 or x>=row or y>=col): return
        if(mat[x][y]!=old_color): return 
        mat[x][y] = new_color
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

    dfs(x,y)
    print(mat)

   
mat = [[1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 0, 0],
       [1, 0, 0, 1, 1, 0, 1, 1],
       [1, 2, 2, 2, 2, 0, 1, 0],
       [1, 1, 1, 2, 2, 0, 1, 0],
       [1, 1, 1, 2, 2, 2, 2, 0],
       [1, 1, 1, 1, 1, 2, 2, 1],
      ]
flood_fill(mat,4,4,3)
