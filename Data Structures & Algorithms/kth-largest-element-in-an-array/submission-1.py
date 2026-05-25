import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #quick select
        k = len(nums) - k

        def quickSelect(left, right):
            pivot = right
            pointer = left

            for i in range(left, right):
                if nums[i] <= nums[pivot]:
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    pointer += 1
            
            # put the pivot into the right place
            nums[pointer], nums[pivot] = nums[pivot], nums[pointer]
            
            if pointer > k:
                return quickSelect(left, pointer - 1)
            elif pointer < k:
                return quickSelect(pointer + 1, right)
            else:
                return nums[pointer]

        return quickSelect(0, len(nums) - 1)


