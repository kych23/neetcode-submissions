class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, 1
        mid_heights = 0
        total = 0
        # Left to Right pass
        while right < len(height):
            if height[right] >= height[left]:
                total += (height[left] * (right - left - 1)) - mid_heights
                left = right
                mid_heights = 0
            else:
                mid_heights += height[right]
            right += 1
        
        # Right to Left pass for the remaining peak
        peak_index = left
        right = len(height) - 1
        left = right - 1
        mid_heights = 0
        while left >= peak_index:
            if height[left] > height[right]:
                total += (height[right] * (right - left - 1)) - mid_heights
                right = left
                mid_heights = 0
            else:
                mid_heights += height[left]
            left -= 1
        
        return total