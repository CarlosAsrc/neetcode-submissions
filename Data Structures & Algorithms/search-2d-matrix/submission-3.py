class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0])-1
        m = 0

        x = 0
        while x < len(matrix):
            if matrix[x][0] <= target <= matrix[x][-1]:
                break
            x+=1
        if x >= len(matrix):
            return False

        while l <= r:
            m = l + ((r-l)//2)
            if matrix[x][m] == target:
                return True
            if matrix[x][m] < target:
                l = m+1
            else:
                r = m-1
        return False
            
