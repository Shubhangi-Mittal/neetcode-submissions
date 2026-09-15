class Solution:
    def decodeString(self, s: str) -> str:
        stck=[]
        for i in range(len(s)):
            if s[i]!="]":
                stck.append(s[i])
            else:
                substr=""
                while stck[-1]!="[":
                    substr=stck.pop()+substr
                stck.pop()

                k=""
                while stck and stck[-1].isdigit():
                    k=stck.pop()+k
                stck.append(int(k)*substr)
        return "".join(stck)
        
