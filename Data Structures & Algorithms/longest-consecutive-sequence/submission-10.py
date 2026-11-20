class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0 
        
        numsSet = set(nums)
        best = 0 

        for num in numsSet:     

            if num - 1 in numsSet: 
                continue
            
            else: 
                current = num
                lenght = 1
                while current + 1 in numsSet: 
                    lenght += 1
                    current += 1
                best = max(best, lenght)
        return best

