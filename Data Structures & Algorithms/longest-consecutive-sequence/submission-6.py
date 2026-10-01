class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums: 
          return 0 
        mi_set = set(nums)
        mejor = 0
        for x in mi_set:  
                if x - 1 in mi_set: 
                    continue
                actual, largo = x, 1
                while actual + 1 in mi_set: 
                    actual += 1
                    largo += 1
                mejor = max(mejor, largo)
        return mejor 


        