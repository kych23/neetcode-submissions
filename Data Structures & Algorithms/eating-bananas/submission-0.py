# Every hour, we eat 'k' bananas. We need to eat all bananas under 'h' hours
# Slowest 'k' = 1
# Fastest 'k' = max(piles)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinishBananas(k: int) -> bool:
            time_elapsed = 0
            for bananas in piles:
                if k > bananas:
                    time_elapsed += 1
                else:
                    time_elapsed += math.ceil((bananas) / k)
            return True if time_elapsed <= h else False

        low, high = 1, max(piles)
        if len(piles) > h:
            return -1
        
        while low <= high:
            middle = low + (high - low) // 2
            if canFinishBananas(middle):
                high = middle - 1
            else:
                low = middle + 1
        
        return low

        
