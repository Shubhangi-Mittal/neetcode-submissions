class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,t in times:
            graph[u].append((v,t))
        mint={}
        minheap=[(0,k)]

        while minheap:
            src_to_cur, cur=heapq.heappop(minheap)
            if cur in mint:
                continue
            
            mint[cur]=src_to_cur
            for nei,nt in graph[cur]:
                if nei not in mint:
                    heapq.heappush(minheap,((src_to_cur+nt),nei))

        if len(mint)==n:
            return max(mint.values())
        else:
            return -1
