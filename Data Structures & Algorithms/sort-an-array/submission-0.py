class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
    
        # Divide the array into two halves
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]
        
        # Recursively sort both halves
        left_sorted = self.sortArray(left_half)
        right_sorted = self.sortArray(right_half)
        
        # Merge the sorted halves
        return self.merge(left_sorted, right_sorted)

    def merge(self, left, right):
        sorted_array = []
        i = j = 0
        
        # Compare elements from both halves and add the smaller one
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
                
        # Append any leftover elements
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])
            
        return sorted_array