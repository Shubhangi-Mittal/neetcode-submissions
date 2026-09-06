class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        fresh=0
        q=deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j)) #append the rotten fruit index to queue
                elif grid[i][j]==1:
                    fresh+=1
        
        if fresh==0:
            return 0
        mins=-1
        while q: #while non empty queue
            q_size = len(q)
            mins+=1
            for _ in range(q_size): #run a loop for length of the size of the queue
                i,j=q.popleft() #pop the left element that is now the new node that becomes rotten and whose neighbors are to be traversed
                for r,c in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]: #check for bounds
                    if 0<=r<rows and 0<=c<cols and grid[r][c]== 1: #check for fresh
                        grid[r][c]=2
                        fresh-=1
                        q.append((r,c)) #if a fresh fruit is made rotten append that node to queue for the bfs loop
        
        if fresh==0:
            return mins
        else:
            return -1