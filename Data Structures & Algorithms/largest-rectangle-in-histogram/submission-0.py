class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stk=[]
        maxarea=0

        for i, h in enumerate(heights):
            start = i
            while stk and h < stk[-1][0]:
                height, j = stk.pop()     # ← not h
                maxarea = max(maxarea, height * (i - j))
                start = j
            stk.append((h, start))
        while stk:
            height,j=stk.pop()
            w=n-j
            maxarea=max(maxarea, height*w)
        return maxarea