class Solution:
    def isValid(self, s: str) -> bool:
        diccionario = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        for i in s: 
            if i in diccionario:
                if stack and diccionario[i] == stack[-1]:
                    stack.pop()
                else: 
                    return False 
            else: 
                stack.append(i)
        return True if not stack else False 

