# two odd length lists

#[1,3,5,7]
#[2,4,6,8,10]
# ans = 5
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ptr1 = 0
        ptr2 = 0
        len1 = len(nums1)
        len2 = len(nums2)
        nums = []
        for i in range(len1 + len2):
            if ptr1 == len1:
                nums.append(nums2[ptr2])
                ptr2 += 1
            elif ptr2 == len2:
                nums.append(nums1[ptr1])
                ptr1 += 1
            else:
                if nums1[ptr1] > nums2[ptr2]:
                    nums.append(nums2[ptr2])
                    ptr2 += 1
                else:
                    nums.append(nums1[ptr1])
                    ptr1 += 1
        med = (len1 + len2) // 2
        if (len1 + len2) % 2 == 0:
            return float(nums[med-1] + nums[med]) / 2.0
        else:
            return float(nums[med])