class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = nums.count(0)
        y=nums.count(1)
        z=nums.count(2)
        for i in range(x):
            nums[i]= 0
        for i in range(x,y+x):
            nums[i]= 1
        for i in range(y+x,z+x+y):
            nums[i] = 2