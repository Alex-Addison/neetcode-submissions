class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if grid == []:
            return grid

        def update(i, j, curr=1):
            if i >= len(grid) or i<0 or j>=len(grid[0]) or j<0 or grid[i][j] == -1 or grid[i][j] == -1:
                return
            if grid[i][j] > curr:
                grid[i][j] = curr
            else:
                return
        
            curr += 1
            update(i+1, j, curr)
            update(i-1, j, curr)
            update(i, j+1, curr)
            update(i, j-1, curr)
            
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    update(i+1, j)
                    update(i-1, j)
                    update(i, j+1)
                    update(i, j-1)




