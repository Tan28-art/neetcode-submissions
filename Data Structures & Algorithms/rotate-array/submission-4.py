class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Intuition here is that for an array like [1,2,3,4] and k = 2
        # first split into 2 sections of k and n-k elements
        # array becomes [1, 2, | 3, 4]
        # Think about final solution for this example
        # It is [3, 4, | 1, 2]
        # Think about the reversed array its [4, 3, | 2, 1]
        # Now notice how the final and reversed arrays are related
        # you just have to reverse the remaining k and n-k elements independently
        
        n = len(nums)
        if k > n:
            k = k % n

        def reverse_array(left, right):
            
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if n != 1 or n != k:
            reverse_array(0, n-1)
            reverse_array(0, k-1)
            reverse_array(k, n-1)

        
        
        

