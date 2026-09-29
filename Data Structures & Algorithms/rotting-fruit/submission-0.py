# multi source bfs
# Start with all rotten fruits (2)
# Each BFS iteration, set fresh fruit (1) neighbors to rotten (2), increment the global "minutes" variable after len(queue)
# has been processed, add neighbors
# once queue is empty, check entire grid and see if there are any fresh fruits left

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1) ]
        minutes = 0
        queue = deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append( (i,j) )
        
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append( (r,c) )
            if queue:
                minutes += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        
        return minutes

