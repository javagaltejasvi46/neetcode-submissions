class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = sorted(set(nums))
        nums[:len(k)]=k
        return len(k)
        