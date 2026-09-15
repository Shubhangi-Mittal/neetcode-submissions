class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stck=[]

        for a in asteroids:
            while stck and a<0 and stck[-1]>0:
                res=a+stck[-1]
                if res<0:
                    stck.pop()
                elif res>0:
                    a=0
                else:
                    a=0
                    stck.pop()
            if a:
                stck.append(a)
        return stck