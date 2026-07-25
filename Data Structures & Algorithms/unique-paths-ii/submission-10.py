class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        print(m,n)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        print(dp)
        if obstacleGrid[0][0] == 1:
            return 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1 or (i==0 and j==0):
                    continue
                print(i, j)
                if i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]