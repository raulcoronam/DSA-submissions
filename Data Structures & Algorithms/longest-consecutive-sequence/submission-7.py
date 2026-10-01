class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        miSet =  set(nums)
        best = 0
        for num in miSet: 
            if num - 1 in miSet: 
                continue
            else: 
                current = num
                lenght = 1
                while current + 1 in miSet: 
                    current += 1
                    lenght += 1
                best = max(best, lenght)
        return best 
