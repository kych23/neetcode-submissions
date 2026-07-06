class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        while k > 0:
            maxCount = None
            for key, value in counts.items():
                if maxCount is None or value > counts[maxCount]:
                    maxCount = key
            result.append(maxCount)
            counts.pop(maxCount)
            k -= 1
        
        return result
