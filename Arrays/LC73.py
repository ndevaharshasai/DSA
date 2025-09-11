class Solution(object):
    def setZeroes(self, matrix):
        zeroes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    zeroes.append([i,j])
        clearedRows = []
        clearedCols = []
        for zero in zeroes:
            x = zero[0]
            y = zero[1]
            if x not in clearedRows:
                matrix[x] = [0 for t in range(len(matrix[x]))]
                clearedRows.append(x)
            if y not in clearedCols:
                i = 0
                while(i<len(matrix)):
                    matrix[i][y]=0
                    i+=1
                clearedCols.append(y)
        
