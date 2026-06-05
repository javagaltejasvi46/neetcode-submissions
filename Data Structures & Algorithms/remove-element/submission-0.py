class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cunt = nums.count(val)
        for _ in range(cunt): 
            nums.remove(val)
        length = len(nums)
        for _ in range(cunt):
            nums.append("_")
        return length       
        