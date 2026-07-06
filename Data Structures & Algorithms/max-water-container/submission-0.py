class Solution:
    def maxArea(self, height: List[int]) -> int:
        line1, line2 = 0, len(height)-1
        maxArea = (height[line1] * (line2 - line1)) if height[line1] < height[line2] else (height[line2] * (line2 - line1))
        while line1 < line2:
            if height[line1] < height[line2]:
                if maxArea < (height[line1] * (line2 - line1)):
                    maxArea = (height[line1] * (line2 - line1))
                line1 += 1
            else:
                if maxArea < (height[line2] * (line2 - line1)):
                    maxArea = (height[line2] * (line2 - line1))
                line2 -= 1

        return maxArea

