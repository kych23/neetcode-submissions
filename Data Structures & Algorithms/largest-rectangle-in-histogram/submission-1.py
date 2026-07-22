# for each index, check every rectangle from [index:] and save max area
# O(n^2) time and O(1) space

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for index, height in enumerate(heights):
            start_index = index
            while stack and stack[-1][1] > height:
              top_index, top_height = stack.pop()
              max_area = max(max_area, top_height * (index - top_index))
              start_index = top_index
            stack.append((start_index, height))
        
        for index, height in stack:
          max_area = max(max_area, height * (len(heights) - index))
        return max_area