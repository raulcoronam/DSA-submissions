class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        output = []

        for word in strs: 
            
            if tuple(sorted(word)) in hashmap: 

                output[hashmap[tuple(sorted(word))]].append(word)
            
            else: 

                hashmap[tuple(sorted(word))] = len(output)
                output.append([word])
        
        return output 