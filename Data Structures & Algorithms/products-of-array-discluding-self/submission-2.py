class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix, total_pre, n = [], 1, len(nums)
        
        for num in nums: 
            total_pre *= num
            prefix.append(total_pre)
        
        postfix, total_post = [0] * len(prefix), 1

        for i in range(n - 1, -1 ,-1):
            total_post *= nums[i]
            postfix[i] = total_post

        output, x = [], 0
        
        while x < n: 
            
            if x == 0: 
                output.append(postfix[x + 1])
            elif x == n - 1: 
                output.append(prefix[x - 1])
            else: 
                output.append(postfix[x + 1] * prefix[x - 1])
            x += 1
        
        return output 
            





