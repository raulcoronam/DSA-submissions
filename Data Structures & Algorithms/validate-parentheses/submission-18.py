class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {")":"(", "}":"{", "]":"["}
        for paren in s: 
            if paren in hashMap: 
                if not stack: 
                    return False
                top = stack.pop()
                if top != hashMap[paren]:
                    return False
            else: 
                stack.append(paren)
        return True if not stack else False