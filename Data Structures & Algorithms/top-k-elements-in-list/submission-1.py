class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}
        
        for num in nums: 
            if num in hashMap: 
                hashMap[num] += 1
            else: 
                hashMap[num] = 1

        sortedMap = sorted(hashMap, key = hashMap.get)
        output = sortedMap[-k::]
        return output       