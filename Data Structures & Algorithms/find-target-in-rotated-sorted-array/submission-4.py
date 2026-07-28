# [3,4,5,6,1,2], target = 6 --> search left side because mid (6) > target (4) and right (2) < middle (6)
# [3,4,5,6,1,2], target = 1 --> search right because mid > target and right < mid
# [2,3,4,5,6,1], target = 5 --> search right because mid < target
# [1,2,3,4,5,6], target = 5 --> search right 
# [6,1,2,3,4,5], target = 5 --> search right 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
          mid = left + (right - left) // 2
          if nums[mid] == target:
            return mid

          if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
              right = mid - 1
            else:
              left = mid + 1
          else:
            if nums[mid] < target <= nums[right]:
              left = mid + 1
            else:
              right = mid - 1
        
        return -1