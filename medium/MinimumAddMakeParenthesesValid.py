class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s) == 0:
            return 0

        # use a stack and iterate through the string
        # if there are remaining open parentheses on the stack at the end, add the nunber of 
        # closing parentheses
        # if stack is empty but see a closing parentheses, add an opening to the beginning of the string

        ret = 0
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) == 0:
                    ret += 1
                else:
                    stack.pop(-1)
            else:
                continue
        
        ret += len(stack)

        return ret
