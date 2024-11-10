class Solution:
    # time complexity is O(n)
    # space complexity is O(n)
    def minRemoveToMakeValid(self, s: str) -> str:
        # Solution 1, slow, 1 way traversal

        # keep a stack of (, and mark the ) for removal whenever it doesn't match
        # remove the remaining ( in the stack, and the marked )

        if len(s) == 0:
            return ""
        if '(' not in s and ')' not in s:
            return s

        stack = []
        indicesToRemove = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) == 0:
                    # remove ')'
                    indicesToRemove.append(i)
                else:
                    stack.pop()

        indicesToRemove = indicesToRemove + stack

        print(indicesToRemove)

        newstr = s
        for i in range(len(s)-1, -1, -1):
            if i in indicesToRemove:
                newstr = newstr[:i] + newstr[i + 1:]

        return newstr
