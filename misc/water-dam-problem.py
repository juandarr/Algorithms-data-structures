'''
Given a non-empty 2D array grid of 0's and 1's, an extension of water is represented by  1's connected 4-directionally (horizontal or vertical.). Find the maximum area of an extension of water in the given 2D array.  
Note: - You may assume all four edges of the grid are surrounded by land. 
          - If there is no water, the maximum area is 0.
          - The length of each dimension in the given grid does not exceed 50.
Example 1:
 
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally. 
 
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.

'''
A = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]

visited = {}

def traverse(i,j):
    D = [-1,1]
    value = 1
    for direction in D:
        if (i+direction >= 0 and i+direction <= len(A)-1) and (i+direction,j) not in visited and A[i+direction][j]==1:
            visited[(i+direction,j)] = 1
            value += traverse(i+direction,j)
            
        if (j+direction >= 0 and j+direction <= len(A[0])-1) and (i,j+direction) not in visited and A[i][j+direction]==1:
            visited[(i,j+direction)] = 1
            value += traverse(i,j+direction)
    return value

max_area = 0    
for i in range(len(A)):
    for j in range(len(A[0])):
        
        if A[i][j]==1 and (i,j) not in visited:
            visited[(i,j)] = 1            
            area = traverse(i,j)
            if area > max_area:
                max_area = area
print(max_area)