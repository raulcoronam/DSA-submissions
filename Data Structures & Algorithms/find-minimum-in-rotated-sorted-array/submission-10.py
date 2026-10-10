class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = nums[l]
        while l <= r: 
            if nums[l] <= nums[r]: 
                minimum = min(minimum, nums[l])
                break
            else: 
                mid = (l + r) // 2
                if nums[mid] >= nums[l]: 
                    l = mid + 1
                else: 
                    minimum = min(minimum, nums[mid])
                    r =  mid - 1
        return minimum

