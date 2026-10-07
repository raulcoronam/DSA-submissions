class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        nums.sort()

        for i, num in enumerate(nums): 
            if i == 0 or nums[i - 1] != nums[i]: 
                L , R = i + 1, n - 1
                while L < R: 
                    if nums[L] + nums[R] > -num:
                        R -= 1

                    elif nums[L] + nums[R] < -num:
                        L += 1

                    else: 
                        output.append([num, nums[L], nums[R]])
                        while  L < R and nums[L] == nums[L+1]:
                            L += 1
                        L += 1
        return output   