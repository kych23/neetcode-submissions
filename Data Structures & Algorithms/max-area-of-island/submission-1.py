class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def bfs(root):
            island_size = 1
            queue = deque( [root] )
            directions = [ (0,1), (0,-1), (1,0), (-1,0) ]
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if (0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1):
                        queue.append( (new_r, new_c) )
                        grid[new_r][new_c] = '0'
                        island_size += 1
            return island_size
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    grid[row][col] = '0'
                    max_area = max(max_area, bfs( (row, col) ))
        
        return max_area