class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        
        # else create hashmap
        countS,countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)

        for c,count in countS.items():
            print(c,count)
            if countS[c] != countT.get(c,0):
                return False
        else:
            return True 

        
        