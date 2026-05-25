class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        else:
            left = 1
            right = 1

            while left < n and right < n:
                if nums[right] == nums[right - 1]:
                    # not unique element, move right, left same
                    right += 1
                else:
                    # element at right is unique so we put element at right on left
                    # and then move both pointers
                    nums[left] = nums[right]
                    left += 1
                    right += 1

            return left