class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj=defaultdict(list)
        for p,c in prerequisites:
            adj[c].append(p)
        pmap={}
        def dfs(crs):
            if crs not in pmap:
                pmap[crs]=set()
                for pr in adj[crs]:
                    pmap[crs]|=dfs(pr)
                pmap[crs].add(crs)
            return pmap[crs]

        for c in range(numCourses):
            dfs(c)
        res=[]
        for u,v in queries:
            res.append(u in pmap[v])
        return res
