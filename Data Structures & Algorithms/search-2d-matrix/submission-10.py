class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])

        low, high = 0, rows - 1
        print(cols)
        while low <= high:
            mid = (low+high) // 2
            print(mid)
            for col in range(cols):
                if matrix[mid][col] == target:
                    return True
            if target > matrix[mid][cols-1]:
                low = mid + 1
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                return False
        return False
        
