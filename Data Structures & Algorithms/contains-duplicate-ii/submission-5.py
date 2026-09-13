class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last={}
        for i,n in enumerate(nums):
            if n in last and i-last[n]<=k:
                return True
            last[n]=i
        return False