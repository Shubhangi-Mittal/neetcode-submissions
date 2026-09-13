class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[[abs(a-x),a] for a in arr]
        heapq.heapify(heap)

        res=[]

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return sorted(res)