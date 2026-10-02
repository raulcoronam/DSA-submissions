class Solution:
    def isPalindrome(self, s: str) -> bool:

        string = "".join([x for x in s if x.isalnum()])
        string_min = string.lower()
        print(string_min)
        izq, der = 0, len(string) -1
        while izq < der:
            if string_min[izq] == string_min[der]:
                izq += 1
                der -= 1
            else:
                return False 
        return True 
        