# Greedy: use ladders on the largest building jumps
# 1. If we have to jump, add it to heap. use ladders if we have any. if we don't have any ladders left, swap the smallest jump seen so far with bricks and add ladder back to "ladders"
# 2. If we don't have to jump, continue in loop

import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []
        
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            
            # Descents are free, skip them
            if climb <= 0:
                continue
            
            # Add this climb to heap (tentatively use a ladder)
            heapq.heappush(min_heap, climb)
            
            # If we still have ladders available, we're good
            if len(min_heap) <= ladders:
                continue
            
            # Out of ladders! Swap smallest climb to use bricks instead
            bricks -= heapq.heappop(min_heap)
            
            # If out of bricks, we're stuck
            if bricks < 0:
                return i
        
        return len(heights) - 1

