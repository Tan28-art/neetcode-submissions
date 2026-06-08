class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}

        for num in nums:
            if not hashmap.get(num):
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        sorted_map = dict(sorted(hashmap.items(), key = lambda x: x[1], reverse=True))

        result = []
        for key, v in sorted_map.items():
            if k == 0:
                break
            result.append(key)
            k -= 1

        return result