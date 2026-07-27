#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] # up, down, left, right
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        result = 0
        h, w = len(grid), len(grid[0]) # height, width
        visited = [[False for _ in range(w)] for  _ in range(h)]
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1' and visited[i][j] == False:
                    # search max connected area
                    # dfs
                    self.dfs(grid, visited, i, j, h, w)
                    # bfs
                    # self.bfs(grid, visited, i, j, h, w)

                    result += 1

        return result


    # Depth-First Search              
    def dfs(self, grid, visited, x, y, h, w):
        
        # Base case
        if grid[x][y] == '0' or visited[x][y]:
            visited[x][y] = True
            return 
        
        # mark currnet cell as visited
        visited[x][y] = True
        
        # explore all four directions
        for d_x, d_y in self.direction:
            next_x = x + d_x
            next_y = y + d_y

            # if the neighbor is within bounds
            if next_x >= 0 and next_x < h and next_y >= 0 and next_y < w:
                # is unvisited land
                if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                    self.dfs(grid, visited, next_x, next_y, h, w)
        
    
    # Breadth first search
    def bfs(self, grid, visited, x, y, h, w):
        
        queue = collections.deque()

        # Start BFS with (x,y) and mark it visited
        queue.append([x,y])
        visited[x][y] = True

        while queue:    
            cx, cy = queue.popleft()
            # Explore all four directions
            for d_x, d_y in self.direction:
                next_x = cx + d_x
                next_y = cy + d_y
                # if the neighbor is within bounds
                if next_x >= 0 and next_x < h and next_y >= 0 and next_y < w:
                    # is unvisited land
                    if grid[next_x][next_y] == '1' and visited[next_x][next_y] == False:
                        queue.append([next_x, next_y])
                        visited[next_x][next_y] = True      
        
# @lc code=end

