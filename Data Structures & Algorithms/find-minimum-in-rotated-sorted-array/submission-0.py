# binary search
# check if middle element > last element
# if greater, we want to check right subarray
# if less than, we want to check left subarray

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        while left < right:
            middle = left + (right - left) // 2
            middle_num = nums[middle]
            if middle_num > nums[-1]:
                left = middle + 1
            elif middle_num <= nums[-1]:
                right = middle
        return nums[left]
