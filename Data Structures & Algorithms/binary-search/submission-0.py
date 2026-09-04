class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarysearch(0,len(nums)-1,nums,target)


    def binarysearch(self, l:int,r:int,nums:List[int], target:int)->int:
        if l>r:
            return -1
        m= l+(r-l)//2

        if nums[m]==target:
            return m
        if nums[m]<target:
            return self.binarysearch(m+1,r,nums,target)
        return self.binarysearch(l,m-1,nums,target)