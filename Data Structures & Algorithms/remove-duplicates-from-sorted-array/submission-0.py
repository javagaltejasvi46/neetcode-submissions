
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = sorted(set(nums))
        nums[:len(result)]=result
        return len(result)
          
        
        
        