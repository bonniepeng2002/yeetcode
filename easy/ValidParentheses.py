class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
                continue
            elif s[i] == ')':
                c = stack.pop()
                if c != '(': 
                    return false
            elif s[i] == ']':
                c = stack.pop()
                if c != '[': 
                    return false
            elif s[i] == '}':
                c = stack.pop()
                if c != '{': 
                    return false
        return true
