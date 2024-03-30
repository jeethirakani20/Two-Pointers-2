#T.C. O(m + n), where m = no of rows, n = no of columns
#S.C O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n - 1

        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j-=1 #move left
            else:
                i+=1 #down
        return False
