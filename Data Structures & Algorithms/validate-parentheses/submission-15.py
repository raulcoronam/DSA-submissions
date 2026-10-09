class Solution:
    def isValid(self, s: str) -> bool:
        mapa = {")" : "(", "}" : "{", "]" : "["}
        resto = []
        for parentheses in s: 
            if parentheses in mapa:
                if resto and mapa[parentheses] == resto[-1]:
                    resto.pop()
                else: 
                    return False 
            else: 
                resto.append(parentheses)    
        return True if not resto else False