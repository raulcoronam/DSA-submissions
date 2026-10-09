class Solution:
    def isValid(self, s: str) -> bool:
        mapa = {")" : "(", "}" : "{", "]" : "["}
        resto = []
        for parentheses in s: 
            if parentheses in mapa:
                if not resto:
                    return False 
                top = resto.pop()
                if top!= mapa[parentheses]: 
                    return False
            else: 
                resto.append(parentheses)    
        return True if not resto else False