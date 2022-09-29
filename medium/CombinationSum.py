class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # this is just DFS! - finding combinations of things that lead to a target
        
        res = []
        tmpSum = []
        self.findSums(candidates, target, res, tmpSum)
        return res
    
    def findSums(self, candidates, target, res, tmpSum):
        if target < 0: return
        if target == 0: 
            res.append(tmpSum)
            return
        for i in range(len(candidates)):
            self.findSums(candidates[i:], target - candidates[i], res, tmpSum+[candidates[i]])
        # if not found for tmpSum, just let tmpSum drop into nothing
        # other recursions will still continue
            
        
        
