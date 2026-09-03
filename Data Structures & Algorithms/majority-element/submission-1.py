class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=defaultdict(int)
        res=cntmx=0

        for i in nums:
            count[i]+=1
            if cntmx<count[i]:
                res=i
                cntmx=count[i]
        return res
        