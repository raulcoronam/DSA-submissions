class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        for num in nums: 
            if num in hashmap: 
                hashmap[num] += 1
            else: 
                hashmap[num] = 1

        sortedMap = sorted(hashmap.items(), key = lambda item:item[1])

        sortedNums = [num[0] for num in sortedMap]

        return sortedNums[-k:]   