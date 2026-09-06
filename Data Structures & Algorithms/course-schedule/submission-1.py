class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #we create a directed graph

        g=defaultdict(list)
        courses=prerequisites
        for a,b in courses:
            g[a].append(b)

        #visited, unvisited, visiting

        unvisited=0
        visiting=1
        visited=2
        states=[unvisited]*numCourses

        #in dfs for the current node take its current state if it is visited hence course can be taken hence return true, else if the state is visiting then return false if current node was set to unvisited now set it to visiting then take all its neighbors from the graph run the same process of dfs on the neighbors if dfs does not return true then return false and set the current node as visited loop for all the nodes that way 

        def dfs(node):
            state=states[node]
            if state==visited:
                return True
            elif state==visiting:
                return False
            states[node]=visiting
            for n in g[node]:
                if not dfs(n):
                    return False
            states[node]=visited
            return True

        # run a dfs on each node for number of courses
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        