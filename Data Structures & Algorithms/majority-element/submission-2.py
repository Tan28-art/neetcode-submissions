class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # More space efficient approach uses boyer-moore algorthm
        # essentially keep count variable, increase for res, dec otherwise
        # if 0 and next element is diff than res, change res and count += 1
        # majority element will outvote the rest of the array

        result = nums[0]
        count = 0
        for num in nums:
            if num == result:
                count += 1

            elif num != result:
                count -= 1
            
            if count == 0:
                result = num
                count += 1

        return result
