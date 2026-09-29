class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows - 1
        while low <= high:
            mid = (low+high) //2
            for col in range(cols):
                if matrix[mid][col] == target:
                    return True
                elif matrix[mid][col] > target:
                    high = mid-1
                elif matrix[mid][col] < target:
                    low = mid+1
        return False