class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            index1 = i

            if diff in hashMap.keys():
                index2 = hashMap[diff]
                break

            hashMap.update({nums[i]: i})

        if index1 > index2:
            temp = index1
            index1 = index2
            index2 = temp
            

        return [index1, index2]
