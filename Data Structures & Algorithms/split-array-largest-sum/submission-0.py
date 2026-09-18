class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)
        res=r
        def canSplit(largest):
            sub=1
            cur=0
            for i in nums:
                cur+=i
                if cur>largest:
                    sub+=1
                    if sub>k:
                        return False
                    cur=i
            return True
        while l<=r:
            m=(l+r)//2
            if canSplit(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res