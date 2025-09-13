class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        changed = []
        for i in range(n):
            for j in range(n):
                if i!=j:
                    if [i,j] not in changed and [j,i] not in changed:
                        matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
                        changed.append([i,j])
                        changed.append([j,i])
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]

        

        