class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return[0]
        
        adj=defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        edges={}
        leaves=deque()

        for src,neigh in adj.items():
            edges[src]=len(neigh)
            if len(neigh)==1:
                leaves.append(src)
        
        while leaves:
            if n<=2:
                return list(leaves)
            for _ in range(len(leaves)):
                leaf=leaves.popleft()
                n-=1
                for i in adj[leaf]:
                    edges[i]-=1
                    if edges[i]==1:
                        leaves.append(i)