from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     result =[]
    #     for i in range(k):
    #         result[i] = max(nums)
    #         self.remove_dup(i,nums)
    #     return result

        
    # def remove_dup(self,ele: int, liss: List[int]) -> List[int]:
    #     while ele in liss:
    #         liss.remove(ele)
    #     return liss

        
        result = [0]*k
        for i in range(len(result)):
            cunt = Counter(nums)
            result[i]=max(cunt,key = cunt.get)
            nums=[x for x in nums if x != result[i]]
        return result 
    
                 