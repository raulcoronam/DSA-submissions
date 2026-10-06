class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs: 
            output += str(len(word)) + "#" + word
        return output

    def decode(self, s: str) -> List[str]:
        output, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            lenght = int(s[i:j])
            word = (s[j + 1 : j + 1 + lenght])
            output.append(word)
            i = j + 1 + lenght
        return output 

