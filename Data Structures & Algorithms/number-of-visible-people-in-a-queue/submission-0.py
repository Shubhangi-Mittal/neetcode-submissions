class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n=len(heights)
        res=[0]*n
        stck=[]

        for i in range(n-1,-1,-1):
            while stck and stck[-1]<heights[i]:
                stck.pop()
                res[i]+=1

            if stck:
                res[i]+=1
            stck.append(heights[i])
        return res