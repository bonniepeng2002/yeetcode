class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        # this question is an interesting application of stacks
        # the stack is used as the final answer, and is manipulated by adding and removing characters
        # the idea is:
        # note the last occurrence of each character
        # iterate through the string
        # if the character is not in the stack, we decide how to add it
        # if this character is SMALLER than the one before it on the stack, and that character on the stack appears elsewhere, then we pop the character(s) on the stack and then add the new small character onto it
        # this works because since the LARGER character appears again, this ensures lexicographical order
        # if it does not appear again, then it MUST stay where it is since we must make a subsequence
        
        if len(s) == 0: return ""
        res = [] # stack
        charDict = {}
        for i in range(0, len(s)):
            charDict[s[i]] = i
        res.append(s[0])
        for i in range(1, len(s)):
            if s[i] in res: continue
            while (len(res) > 0 and s[i] < res[-1] and i < charDict[res[-1]]):
                res.pop()            
            res.append(s[i])
        return ''.join(res)
                
                
            
