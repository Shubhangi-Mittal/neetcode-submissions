class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=[[] for _ in range(n)]
        for u,v,price in flights:
            adj[u].append([v,price])
        dist=[[float("inf")]*(k+5) for _ in range(n)]

        dist[src][0]=0
        minheap=[(0,src,-1)]
        while minheap:
            cost,node,stops=heapq.heappop(minheap)
            if dst==node: return cost
            if stops==k or dist[node][stops+1]<cost:
                continue
            for nei,w in adj[node]:
                nextcost=cost+w
                nextstops=1+stops
                if dist[nei][nextstops+1]>nextcost:
                    dist[nei][nextstops+1]=nextcost
                    heapq.heappush(minheap,(nextcost,nei,nextstops))
        return -1