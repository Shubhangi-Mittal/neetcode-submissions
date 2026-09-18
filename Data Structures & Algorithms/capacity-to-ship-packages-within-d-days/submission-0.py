class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)

        res=r

        def canShip(cap):
            ships=1
            current_capacity=cap
            for w in weights:
                if current_capacity-w<0:
                    ships+=1
                    current_capacity=cap
                current_capacity-=w
            return ships<=days

        while l<=r:
            capacity=(l+r)//2
            if canShip(capacity):
                res=min(res,capacity)
                r=capacity-1
            else:
                l=capacity+1
        return res