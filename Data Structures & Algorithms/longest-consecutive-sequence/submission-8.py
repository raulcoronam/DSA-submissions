class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        if not nums: 
            return 0 
        
        clean = set(nums)

        best = 0

        for num in clean: 
            if num - 1 in clean: 
                continue
            else: 
                current = num
                lenght = 1
                while current + 1 in clean: 
                    lenght += 1
                    current += 1
                best = max(best, lenght)
        
        return best



             