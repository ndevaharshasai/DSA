class Solution(object):
    def searchMatrix(self, matrix, target):
        i = 0
        while(i<len(matrix) and matrix[i][0]<=target):
            i+=1
        i-=1
        if target in matrix[i]:
            return True
        return False