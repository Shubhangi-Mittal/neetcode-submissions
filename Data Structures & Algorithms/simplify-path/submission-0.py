class Solution:
    def simplifyPath(self, path: str) -> str:
        stck=[]
        paths=path.split("/")
        for c in paths:
            if c=="..":
                if stck:
                    stck.pop()
            elif c!="" and c!=".":
                stck.append(c)

        return "/"+"/".join(stck)