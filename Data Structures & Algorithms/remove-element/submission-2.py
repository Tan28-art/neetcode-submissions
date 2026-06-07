class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        n = len(nums)
        right = n -1

        while left <= right:
            if nums[left]==val:
                # swap the element to the end of the list
                # here i just replace the left invalid element, with the one at right
                # This loses the value of the invalid element, but ig we do not care 
                # more efficient as we do not have to do the second write.
                nums[left] =  nums[right]

                # move right pointer behind
                right -= 1

                # dont move left cause we still have to check left element
            else:
                left += 1

        return right + 1