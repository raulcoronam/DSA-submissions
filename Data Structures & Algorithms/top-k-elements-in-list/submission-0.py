class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = {}
        
        for num in nums: 
            if num in hashMap: 
                hashMap[num] += 1
            else: 
                hashMap[num] = 1

        sortedMap = sorted(hashMap.items(), key = lambda item:item[1])

        sortedNums = [num[0] for num in sortedMap]

        return sortedNums[-k:]