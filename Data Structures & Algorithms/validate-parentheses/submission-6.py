class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        order = {")":"(", "}":"{", "]":"["}
        for i in s:
            n = len(stack)
            if i == "{" or i == "(" or i == "[":
                stack.append(i) 
            elif (n > 0) and (order[i] == stack[-1]): 
                stack.pop() 
            else: 
                return False
        if stack: 
                return False
        else: 
            return True  

        

"""

Lo último que se abrió debe ser lo primero que se cierre

"""