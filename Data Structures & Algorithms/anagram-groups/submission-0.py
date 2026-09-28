class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        f_List = []
        for anagram in strs: 
            if tuple(sorted(anagram)) in hashMap: 
                f_List[hashMap[tuple(sorted(anagram))]].append(anagram)
            else:
                hashMap[tuple(sorted(anagram))] = len(f_List)
                f_List.append([anagram])
        return f_List