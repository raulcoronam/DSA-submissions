class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  
        can_nums = sorted(set(nums))
        counter = 1
        max_streak = 1
        for i in range(len(can_nums) - 1): 
            if can_nums[i] + 1 == can_nums[i + 1]:
                counter += 1
                max_streak = max(counter, max_streak)
            else: 
                counter = 1
        return max_streak 
