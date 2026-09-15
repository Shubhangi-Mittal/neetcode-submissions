class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta=defaultdict(int)

        for s,d in trust:
            delta[s]-=1
            delta[d]+=1

        for i in range(1,n+1):
            if delta[i]==n-1:
                return i
        return -1