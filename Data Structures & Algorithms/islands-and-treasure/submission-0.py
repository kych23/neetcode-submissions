# for each 0 cell, perform BFS layer by layer
#   For each iteration of BFS, you want to set any non-zero cells to min(iteration_num + 1, current_cell_state)
# return grid

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 2147483647:
                    grid[new_row][new_col] = grid[row][col] + 1
                    queue.append((new_row, new_col))