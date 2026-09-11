class Solution:
    def isValid(self, s: str) -> bool:
        diccionario = {")" : "(" , 
                       "]" : "[", 
                       "}" : "{"}
        open_brackets = []
        for i in s: 
            if i in diccionario and open_brackets: 
                if diccionario[i] == open_brackets[-1]:
                    open_brackets.pop()
                else: 
                    return False 
            else: 
                open_brackets.append(i)
        return True if not open_brackets else False
