class Solution:
    def validPalindrome(self, s: str) -> bool:
        # try to remove every letter, and compare the string and its reverse.
        # sounds very ineffective but it's still O(n)

        # if s == s[::-1]:
        #     return True

        # for i in range(len(s)):
        #     newstr = s[:i] + s[i+1:]
        #     if newstr == newstr[::-1]:
        #         return True

        # return False

        # two pointers. Once it hits a difference, try for palindrome by removing either one

        ptr1 = 0
        ptr2 = len(s) - 1

        while ptr1 < ptr2:
            if s[ptr1] != s[ptr2]:
                removal1 = s[:ptr1] + s[ptr1 + 1:]
                removal2 = s[:ptr2] + s[ptr2 + 1:]
                if removal1 == removal1[::-1] or removal2 == removal2[::-1]:
                    return True
                else:
                    return False

            ptr1 += 1
            ptr2 -= 1
        
        return True
