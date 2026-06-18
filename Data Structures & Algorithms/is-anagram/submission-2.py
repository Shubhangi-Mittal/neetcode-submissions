class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        
        countS, countT={},{} #hashmaps
        for i in range(len(s)):#since both have same lengths
            countS[s[i]]=1+countS.get(s[i],0) #countS of ith character in S in hashmap, 
            #get just gives the default value to be zero 
            #if it doesnt already exist in the hashmap
            countT[t[i]]=1+countT.get(t[i],0)
        for c in countS: #checking counts of each character in the hashmap
            if countS[c]!=countT.get(c,0):
                return False
        
        return True
        