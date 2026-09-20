class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS,COLS=len(heights),len(heights[0])
        minheap=[[0,0,0]]
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        visit=set()
        while minheap:
            diff,r,c=heapq.heappop(minheap)
            if (r,c) in visit:
                continue
            visit.add((r,c))
            if (r,c)==(ROWS-1,COLS-1):
                return diff
            for dr,dc in directions:
                newR,newC=r+dr,c+dc
                if (newR<0 or newC<0 or newR>=ROWS or newC>=COLS or (newR,newC) in visit):
                    continue
                newdiff=max(diff,abs(heights[r][c]-heights[newR][newC]))
                heapq.heappush(minheap,[newdiff,newR,newC])
        return 0