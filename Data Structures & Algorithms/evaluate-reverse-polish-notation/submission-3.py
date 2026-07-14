class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["+", "-", "*", "/"])
        stack = []
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                result = 0
                if t == "+":
                    result += op1 + op2
                elif t == "-":
                    result += op1 - op2
                elif t == "*":
                    result += op1 * op2
                elif t == "/":
                    result += int(float(op1) / op2)
                stack.append(result)
        return int(stack[-1])