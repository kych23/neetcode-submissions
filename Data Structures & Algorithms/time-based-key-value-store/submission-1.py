# key: [(ts, value), (ts, value)]
# get() find the key, start at index 0 (highest ts) and keep going right until you get the largest ts < 'timestamp'

# optimized: set always appends to end of list
# optimized: get always uses binary search to find the 

from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ts_values = self.map[key]
        return self._binary_search(ts_values, timestamp)
        
    def _binary_search(self, array, timestamp):
        res = ""
        left, right = 0, len(array) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if array[mid][0] <= timestamp:
                res = array[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res
