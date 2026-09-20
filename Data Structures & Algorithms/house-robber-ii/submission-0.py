class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.hr1(nums[1:]),self.hr1(nums[:-1]))
    
    def hr1(self,nums):
        r1,r2=0,0
        for i in nums:
            t=max(i+r1,r2)
            r1=r2
            r2=t
        return r2

