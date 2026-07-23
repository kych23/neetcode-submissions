class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            middle = left + (right - left) // 2
            if matrix[middle // n][middle % n] < target:
                left = middle + 1
            elif matrix[middle // n][middle % n] > target:
                right = middle -1
            else:
                return True

        return False