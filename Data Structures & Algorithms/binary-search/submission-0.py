class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R: 
            if nums[L] == target: 
                return L
            elif nums[R] == target: 
                return R 
            else: 
                L += 1
                R -= 1
        return -1 
