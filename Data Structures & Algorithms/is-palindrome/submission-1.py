class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(c for c in s if c.isalnum()).lower()     
        n = len(clean)
        L, R = 0, n - 1
        print(clean)  
        while L < R: 
            if clean[L] == clean[R]:
                L += 1
                R -= 1
            else: 
                return False 
        return True     
