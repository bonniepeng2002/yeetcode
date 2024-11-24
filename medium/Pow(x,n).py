class Solution:
    def myPow(self, x: float, n: int) -> float:
        # iterating n times is too many
        # the idea is to limit the number of times recursion has to run, by half
        # this means that whenever n is even, you can do quicker math by pre-exponenting it before putting it
        # into recursion

        # (2^x)^n/x = 2^n

        if n == 0:
            return 1
        
        if n < 0:
            x = 1/x
            n *= -1

        if n%2 == 0:
            return self.myPow(x * x, n/2)
        else:
            return x * self.myPow(x, n-1)
