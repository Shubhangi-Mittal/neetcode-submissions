class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        indegree=[0]*numCourses

        for a,b in prerequisites:
            g[b].append(a)
            indegree[a]+=1

        q=deque(i for i in range(numCourses) if indegree[i]==0)
        order=[]

        taken=0
        while q:
            node=q.popleft()
            order.append(node)
            taken+=1
            for n in g[node]:
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)
        
        return order if len(order)==numCourses else []
    