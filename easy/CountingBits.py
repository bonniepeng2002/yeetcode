class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        answer = []
        for i in range(0,n+1):
            binary = bin(i)[2:] # converts i to binary, and cuts off the first 2 chars
            answer.append(sum(int(x) for x in binary)) # sums up the digits
        return answer
            
