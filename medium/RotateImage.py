class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # to rotate clockwise, reverse the order the numbers appear in the columns, then reflect on the diagonal (swag symmetry)
        # if rotating counterclockwise, reverse the rows, then reflect
        for col in range(n):
            for row in range(n/2):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[n-1-row][col]
                matrix[n-1-row][col] = tmp
        for row in range(n):
            for col in range(n):
                if row == col: 
                    break
                tmp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = tmp
                    
                
