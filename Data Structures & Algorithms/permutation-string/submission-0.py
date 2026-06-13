from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1=Counter(s1)
        
        l=0
        r=len(s1)-1
        while r<len(s2):
            length = len(set1)
            temp = s2[l:r+1]
            if Counter(temp) == set1:
                return True
            l+=1
            r+=1
        return False 


        

        