class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair:pair[0])
        op=[intervals[0]]

        for s,e in intervals:
            le=op[-1][1]
            if s<=le:
                op[-1][1]=max(le,e)
            else:
                op.append([s,e])
        return op