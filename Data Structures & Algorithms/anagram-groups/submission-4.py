class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        output = []
        count = 0
        for i, word in enumerate(strs): 
            if str(sorted(word)) in hashMap: 
                output[hashMap[str(sorted(word))]].append(word)
            else: 
                hashMap[str(sorted(word))] = count
                count += 1 
                output.append([word]) 
        return output      

        