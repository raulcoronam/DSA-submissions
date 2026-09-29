class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        total_pre, total_post = 1, 1
        n = len(nums)
        
        for i in range(n):
            total_pre *= nums[i]
            prefix.append(total_pre)

        postfix = [0] * len(prefix)    

        for i in range(n - 1, -1, -1):
            total_post *= nums[i]
            postfix[i] = total_post
        
        output = []
        for i in range(n): 
            if i == 0: 
                output.append(postfix[i + 1])

            elif i >= n - 1: 
                output.append(prefix[i - 1])
                
            else: 
                output.append(prefix[i - 1] * postfix[i + 1])

        return output

