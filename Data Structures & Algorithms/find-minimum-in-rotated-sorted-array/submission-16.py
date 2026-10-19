class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        output = nums[low]
        while low <= high: 
            mid = (low + high) // 2
            
            if output <= nums[mid]:  
                low = mid + 1
            
            else: 
                output = nums[mid]
                high = mid - 1
            
        return output 