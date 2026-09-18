class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [len(heights)-1]
        maxHeight = heights[-1]
        for i in range(n - 2, -1, -1):
            if heights[i] > maxHeight:
                res.append(i)
                maxHeight = heights[i]
        return res[::-1]
