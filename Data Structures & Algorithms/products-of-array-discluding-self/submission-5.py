class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums) 

        totalPre, prePro = 1, []

        for num in nums: 

            totalPre *= num
            prePro.append(totalPre)

        totalPost, postPro = 1, [0] * n

        for i in range(n - 1, -1, -1):

            totalPost *= nums[i] 
            postPro[i] = totalPost

        output = []

        for i in range(n): 
            if i == 0: 
                output.append(postPro[i + 1])
            elif i >= n - 1: 
                output.append(prePro[i - 1])
            else: 
                output.append(prePro[i - 1] * postPro[i + 1])
    
        return output




