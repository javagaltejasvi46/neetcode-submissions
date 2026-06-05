from collections import Counter
class Solution:    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for strr in strs:
            key="".join(sorted(strr))
            if key not in dict1 :dict1[key]=[]
            dict1[key].append(strr)
        
        result = list(dict1.values())
        return result 
