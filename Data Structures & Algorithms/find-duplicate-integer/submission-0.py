class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashMap = {}

        for i in range(0, len(nums)):
            if nums[i] in hashMap.keys():
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1

        for k, v in hashMap.items():
            if v > 1:
                return k