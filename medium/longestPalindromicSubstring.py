class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ""
        
        longest = s[0]
        
        # odd length palindrome
        for i in range(1, len(s)):
            j = 1
            while (i-j >= 0 and i+j < len(s) and s[i-j] == s[i+j]):
                if (len(s[i-j:i+j+1]) > len(longest)):
                    longest = s[i-j:i+j+1]
                j += 1
                
        # even length palindrome
        for i in range(0, len(s)):
            j = 1
            if (i+1 < len(s) and s[i] == s[i+1]):
                if (len(longest) < 2): longest = s[i:i+2]
                while (i-j >= 0 and i+j+1 < len(s) and s[i-j] == s[i+1+j]):
                    if (len(s[i-j:i+j+2]) > len(longest)):
                        longest = s[i-j:i+j+2]
                    j += 1
            
            
        return longest
                
