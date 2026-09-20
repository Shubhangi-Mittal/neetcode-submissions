class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        dp=[[float("inf")]*(c+1) for _ in range(r+1)]
        dp[0][1]=0

        for i in range(1,r+1):
            for j in range(1,c+1):
                dp[i][j]=grid[i-1][j-1]+min(dp[i-1][j],dp[i][j-1])
        return dp[r][c]