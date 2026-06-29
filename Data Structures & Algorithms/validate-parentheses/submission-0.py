class Solution:
    def isValid(self, s: str) -> bool:
        # Pushdown Automata + Balancing Parentheses
        # The basic idea is using a stack to keep track of the current bracket type
        # then searching the string for the closing bracket that matches the top of the stack.
        stack = collections.deque()
        match_bracket = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            # Found closing bracket, need to check order
            if c in match_bracket:
                # Opening bracket at top of stack matches the found closing bracket.
                if stack and stack[-1] == match_bracket[c]:
                    stack.pop()
                else:
                    # Wrong order (e.g. stack = '(', = '}')
                    return False
            else:
                # c is an opening bracket, add it to the stack.
                stack.append(c)
        
        # If stack is not empty, string isn't balanced.
        return True if not stack else False
        

