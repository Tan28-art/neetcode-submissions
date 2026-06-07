class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        n = len(nums)
        right = n -1

        while left <= right:
            if nums[left]==val:
                # swap the element to the end of the list
                nums[left], nums[right] = nums[right], nums[left]

                # move right pointer behind
                right -= 1

                # dont move left cause we still have to check left element
            else:
                left += 1

        return right + 1