class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        boxes = [[] for _ in range(9)]

        def getBox(i, j):
            return 3*(i//3) + j//3

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.': continue
                if num not in rows[i] and num not in cols[j] and num not in boxes[getBox(i,j)]:
                    rows[i].append(num)
                    cols[j].append(num)
                    boxes[getBox(i,j)].append(num)
                else:
                    return False

        return True