class Solution:
    def climbStairs(self, n: int) -> int:
        c=[-1]*n
        def dfs(i):
            if i>=n:
                return i==n
            if c[i]!=-1:
                return c[i]
            c[i]=dfs(i+1)+dfs(i+2)
            return c[i]
        return dfs(0)