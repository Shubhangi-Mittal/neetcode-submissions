class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda t: t[1])#sort the trips with starting position

        minHeap=[] #has end value and number os passengers
        curr=0

        for t in trips:
            num, start, end=t
            while minHeap and minHeap[0][0]<=start:
                curr-=minHeap[0][1]
                heapq.heappop(minHeap)

            curr+=num
            if curr>capacity:
                return False
            heapq.heappush(minHeap,[end,num])
        return True