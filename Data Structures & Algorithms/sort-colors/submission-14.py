class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # keep track of the first zero?
        # three pointer approach
        left = 0
        right = len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == 0:
                # swap i and l
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                # swapped element needs to be checked
            else:
                i += 1
            


