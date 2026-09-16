class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p=[i for i in range(n)]
        r=[1]*n
        def find(n1):
            res=n1
            while res!=p[res]:
                p[res]=p[p[res]]
                res=p[res]
            return res

        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return 0
            if r[p2]>r[p1]:
                p[p1]=p2
                r[p2]+=r[p1]
            else:
                p[p2]=p1
                r[p1]+=r[p2]
            return 1

        res=n
        for n1,n2 in edges:
            res-=union(n1,n2)
        return res