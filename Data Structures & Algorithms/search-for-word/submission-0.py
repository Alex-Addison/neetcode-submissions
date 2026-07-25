class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        starts = []

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    starts.append((row, col))

        found = False
        def dfs(string, row, col, cells):
            print(string)
            if string == word:
                nonlocal found
                found = True
                return
            cells.append((row,col))
            if row+1<len(board) and (row+1, col) not in cells:
                dfs(string+board[row+1][col], row+1, col, cells)
            if row-1>=0 and (row-1, col) not in cells:
                dfs(string+board[row-1][col], row-1, col, cells)
            if col+1<len(board[0]) and (row, col+1) not in cells:
                dfs(string+board[row][col+1], row, col+1, cells)
            if col-1>=0 and (row, col-1) not in cells:
                dfs(string+board[row][col-1], row, col-1, cells)
            cells.remove((row,col))


        for start in starts:
            dfs(word[0], start[0], start[1], [])
                
        return found