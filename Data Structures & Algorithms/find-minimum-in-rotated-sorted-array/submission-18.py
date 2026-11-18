class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        output = nums[l]

        while l <= r:
            mid = (l + r) // 2  
            if output <= nums[mid]: 
                l = mid + 1
            else: 
                output = nums[mid]
                r = mid - 1
        return output 
