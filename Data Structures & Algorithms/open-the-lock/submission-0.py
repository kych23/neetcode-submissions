# Graph starting at (0,0,0,0) where each edge increments an index by +/- 1. BFS from (0,0,0,0) to target

# time: O(1)
# space: O(1)

import collections
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        
        deadends_set = set(deadends)
        if '0000' in deadends_set:
            return -1
        
        queue = deque(['0000'])
        visited = {'0000'}
        turns = 0
        
        while queue:
            turns += 1
            for _ in range(len(queue)):  # Process current level
                lock = queue.popleft()
                
                for i in range(4):  # Iterate over 4 wheels
                    for delta in [1, -1]:  # Up or down
                        digit = str((int(lock[i]) + delta + 10) % 10)
                        next_lock = lock[:i] + digit + lock[i+1:]
                        
                        if next_lock == target:
                            return turns
                        if next_lock not in visited and next_lock not in deadends_set:
                            visited.add(next_lock)
                            queue.append(next_lock)

        return -1