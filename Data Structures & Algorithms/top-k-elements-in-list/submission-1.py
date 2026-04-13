class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        sorted_tuple = (sorted(hashmap.items() ,reverse= True, key=lambda x : x[1]))

        res = []
        for i in range(k):
            res.append(sorted_tuple[i][0])
        
        return res
