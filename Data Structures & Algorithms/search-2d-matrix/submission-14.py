class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows-1


        while l<= r:
            m = (l+r) //2
            for col in range(cols):
                if matrix[m][col] == target:
                    return True
            if target >= matrix[m][cols-1]:
                l = m + 1
            elif target<= matrix[m][0]:
                r = m - 1
            else:
                return False
        return False
