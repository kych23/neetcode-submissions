# Naive solution: For each element in temperatures, look at every index after current, 
# where once we find a value greater than current, we set the number of jumps to a new output array.
# If we reach the end without finding a higher temperature, we set the value to 0
# Time: O(n^2)
# Space: O(1)

# Optimized solution:
# maintain a stack that has the indexes of the value we checked. 
# For each value in temperatures (left -> right):
#   while this value is > stack[-1]:
#       index = stack.pop()
#       result[index] = curr_index - index
#   stack.append(curr_index)
# return result

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, num in enumerate(temperatures):
            while stack and num > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result


