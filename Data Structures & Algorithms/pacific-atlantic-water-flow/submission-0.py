class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_que=deque()
        p_seen=set()

        a_que=deque()
        a_seen=set()

        rows=len(heights)
        cols=len(heights[0])

        #ignoring the top wall for pacific ocea
        for j in range(cols):
            p_que.append((0,j))
            p_seen.add((0,j))

        #ignoring the left wall for the pacific ocean
        for i in range(1,rows):
            p_que.append((i,0))
            p_seen.add((i,0))

        #ignoring the right wall
        for i in range(rows):
            a_que.append((i,cols-1))
            a_seen.add((i,cols-1))

        #ignoring bottom wall
        for j in range(cols):
            a_que.append((rows-1,j))
            a_seen.add((rows-1,j))

        def get_coords(que,seen):
            coords=set()
            while que:
                i,j=que.popleft()
                coords.add((i,j))
                for i_off,j_off in [(0,1),(1,0),(0,-1),(-1,0)]:
                    r,c=i+i_off,j+j_off
                    if 0<=r<rows and 0<=c<cols and heights[r][c]>=heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        que.append((r,c))
            return coords

        p_coords=get_coords(p_que,p_seen)
        a_coords=get_coords(a_que,a_seen)
        return list(p_coords.intersection(a_coords))