class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]!=1:
                return 0
            else:
                grid[i][j]= 0
                return (1+ dfs(i,j+1)+
                dfs(i+1,j)+
                dfs(i,j-1)+
                dfs(i-1,j))

        area_max=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    area_max=max(area_max, dfs(i,j))

        return area_max
        