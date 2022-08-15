class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arr = [[] for i in range(numRows)] # repeats [] n times
        row = -1;
        increasing = True
        for i in range(len(s)):
            if (row == numRows - 1):
                increasing = False
            elif (row == 0):
                increasing = True
                
            if (increasing):
                row += 1
            else:
                row -= 1
            
            if (numRows == 1): # special case
                row = 0
                
            arr[row].append(s[i])
            
        ans = ""
        for i in range(numRows):
            str = ''.join(arr[i])
            ans += str
        return ans
