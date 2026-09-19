class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsindx={n:i for i,n in enumerate(nums1)}
        res=[-1]*len(nums1)

        stck=[]
        for i in range(len(nums2)):
            cur=nums2[i]
            while stck and cur>stck[-1]:
                val=stck.pop()
                idx=numsindx[val]
                res[idx]=cur
            if cur in numsindx:
                stck.append(cur)
        return res