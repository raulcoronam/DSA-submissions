class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(a.lower() for a in s if a.isalnum())
        print(clean_s)
        l, r = 0, len(clean_s) - 1

        while l <= r: 
            if clean_s[l] is clean_s[r]: 
                l += 1
                r -= 1
            else: 
                return False
        return True     