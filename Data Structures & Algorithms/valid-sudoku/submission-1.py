class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if elem != '.':
                    sq = (i // 3) * 3 + (j // 3)

                    if elem in squares[sq] or elem in rows[i] or elem in cols[j]:
                        return False
                    
                    squares[sq].add(elem)
                    rows[i].add(elem)
                    cols[j].add(elem)

        return True
                    
                    