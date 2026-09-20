class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res=0
        pend=intervals[0][1]
        for start,end in intervals[1:]:
            if start>=pend:
                pend=end
            else:
                res+=1
                pend=min(end,pend)
        return res