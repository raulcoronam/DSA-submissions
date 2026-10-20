class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        
        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target: 
                return mid

            # target = 4  
            # [0, 1, 2, 3, 4, 5, 6]
            # [l       mid       r]
            # target = 0
            # [3, 4, 5, 6, 0, 1, 2]
            # [l       mid       r]
            
            # left sorted
            elif nums[l] <= nums[mid]:

                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else: 
                    r = mid - 1
            
            # target = 4
            # [4, 5, 0, 1, 2, 3]
            # target = 0
            # [0, 1, 2, 3, 4, 5]
            # right sorted
            else:
                if nums[r] < target or target < nums[mid]: 
                    r = mid - 1
                else: 
                    l = mid + 1

        return -1








