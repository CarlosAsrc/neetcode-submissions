class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, column, square = {}, {}, {}
        for i in range(9):
            row[i] = set()
            column[i] = set()
            square[i] = set()

        for ir, r in enumerate(board):
            for ic, c in enumerate(r):
                if c == '.':
                    continue
                c = int(c)
                if c < 0 or c > 9:
                    return False
                if c in row[ir]:
                    return False
                if c in column[ic]:
                    return False
                if c in square[ (ir//3)*3 + (ic//3) ]:
                    return False
                
                row[ir].add(c)
                column[ic].add(c)
                square[ (ir//3)*3 + (ic//3) ].add(c)
        return True

        