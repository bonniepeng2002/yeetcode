class Solution(object):
    def addParentheses(self, res, myStr, open, close, n):
        if len(myStr) == n*2: 
            res.append(myStr)
        
        if open < n:
            self.addParentheses(res, myStr+'(', open+1, close, n)
        if open > close:
            self.addParentheses(res, myStr+')', open, close+1, n)
            
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        # this solution is so impressive
        # the main idea is that in the recursion, something will always execute before another thing
        # we use this to our advantage, by saying that we add a ( to the string before we go and add a ) to create a new base
        
        myStr = ""
        res = []
        self.addParentheses(res, myStr, 0, 0, n)
        return res
        
    
