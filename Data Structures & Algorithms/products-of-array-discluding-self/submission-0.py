class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            output.append(prefix)
            prefix *= nums[i]
        for i in range(len(nums)):
            output[len(nums)-1-i] *= suffix
            suffix *= nums[len(nums)-1-i]
        return output