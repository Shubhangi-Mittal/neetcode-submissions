class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)

        tasks.sort(key=lambda t: t[0]) #tasks[enquetime][processing time]
        res=[]
        minHeap=[]
        i=0
        time=tasks[0][0] #task with minimum enqueue time

        while minHeap or i<len(tasks):
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1],tasks[i][2]]) #ith task's processing time and index
                i+=1
            if not minHeap:
                time=tasks[i][0]
            else:
                processTime, index=heapq.heappop(minHeap)
                time+=processTime
                res.append(index)
        
        return res

        