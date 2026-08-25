class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        line_set = set()
        column_sets = {x: [] for x in range(9)}
        square_sets = {x: [] for x in range(9)}
        

        for ii, i in enumerate(board):
            line_set = set()
            for ij, j in enumerate(i):
                if j == '.':
                    continue
                if (int(j) < 0 or int(j) > 9):
                    return False
                if j in line_set:
                    return False
                if j in column_sets[ij]:
                    return False
                square_index = (ii//3) * 3 + (ij//3)
                if j in square_sets[square_index]:
                    return False
                square_sets[square_index].append(j)
                line_set.add(j)
                column_sets[ij].append(j)
        


        return True

        