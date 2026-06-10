class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        w = len(matrix[0])
        h = len(matrix)
        
        l = 0
        r = w * h - 1

        while l <= r:
            mid = (l + r) // 2
            m_row, m_colomn = mid // w, mid % w
            if matrix[m_row][m_colomn] == target:
                return True
            elif matrix[m_row][m_colomn] < target:
                l = mid + 1
            else:
                r = mid - 1 
        return False