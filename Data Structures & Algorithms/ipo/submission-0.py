class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxp=[]
        minc=[(c,p) for c,p in zip(capital,profits)]

        heapq.heapify(minc)
        for i in range(k):
            while minc and minc[0][0]<=w:
                c,p=heapq.heappop(minc)
                heapq.heappush(maxp,-p)
            if not maxp:
                break
            w+=-1*heapq.heappop(maxp)
        return w