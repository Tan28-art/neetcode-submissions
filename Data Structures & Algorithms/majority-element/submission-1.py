class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if hashmap.get(num):
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        max_val = hashmap[nums[0]]
        result = nums[0]

        for k, v in hashmap.items():
            if v > max_val:
                max_val = v
                result = k

        return result
