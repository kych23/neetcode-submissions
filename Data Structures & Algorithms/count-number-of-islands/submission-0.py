class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(root):
            directions = [ (-1,0), (1,0), (0, 1), (0,-1) ]
            queue = deque([root])
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1'):
                        grid[nr][nc] = '2'
                        queue.append( (nr,nc) )

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    result += 1
                    # grid[row][col] = '2'
                    bfs( (row, col) )

        return result