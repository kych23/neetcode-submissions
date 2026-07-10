
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for letter in s:
            if letter in mapping and len(stack) > 0:
                if stack[-1] == mapping[letter]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(letter)
        return len(stack) == 0