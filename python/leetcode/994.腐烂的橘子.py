#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#

# @lc code=start
class Solution:
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] # up, down, left, right
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # Use Multi-source BFS to simulate the process of oranges becoming rotten

        m, n = len(grid), len(grid[0])

        # Queue stores the coordinates of all currently rotten oranges
        queue = collections.deque()  
        # Count the number of fresh oranges
        num_fresh = 0  

        # Initialize BFS queue and count fresh oranges
        for i in range(m):
            for j in range(n):
                # Add all rotten oranges as the starting points of BFS
                if grid[i][j] == 2:
                    queue.append([i, j])
                # Count fresh oranges
                elif grid[i][j] == 1:
                     num_fresh += 1

        # Edge cases
        # If there are no fresh oranges, no time is needed
        if num_fresh == 0:
            return 0 
        # # If there are fresh oranges but no rotten oranges,  
        if len(queue) == 0:
            return -1

        # Track the elapsed time
        time = -1
        while queue:
            # Process all oranges that become rotten at the current minute
            level_size = len(queue)
            for _ in range(level_size):  
                cx, cy = queue.popleft()
                # explore four direciton
                for dx, dy in self.direction:
                    next_x = cx + dx
                    next_y = cy + dy
                    # Check whether the neighbor is inside the grid
                    if next_x >=0 and next_x < m and next_y >=0 and next_y < n:
                         # If the neighbor is a fresh orange,
                        # it becomes rotten in the next minute
                       if grid[next_x][next_y] == 1:
                            queue.append([next_x, next_y])
                            # Mark it as rotten
                            grid[next_x][next_y] = 2
                            # Decrease remaining fresh oranges count
                            num_fresh -= 1
            
            # One BFS layer represents one minute
            time += 1

        # If some fresh oranges remain, they cannot be reached
        # Otherwise, return the total time required
        return -1 if num_fresh > 0 else time                 
        
# @lc code=end

