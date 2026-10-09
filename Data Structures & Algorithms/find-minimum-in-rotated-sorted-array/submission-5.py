class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        output = nums[low]
        while low <= high:
            if nums[low] <= nums[high]: 
                output = min(output, nums[low])
                break
            else: 
                m = (low + high) // 2
                if nums[m] >= nums[low]:
                    low = m + 1 
                else: 
                    output = min(output, nums[m])
                    high = m - 1 

        
        return output 

        