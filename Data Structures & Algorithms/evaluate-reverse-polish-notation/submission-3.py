class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens:
            if element not in {"+", "-", "/", "*"}:
                stack.append(int(element))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if element == "+":
                    stack.append(operand1 + operand2)
                elif element == "-":
                    stack.append(operand1 - operand2)
                elif element == "*":
                    stack.append(operand1 * operand2)
                else:
                    stack.append(int(operand1 / operand2))
        return int(stack[0])