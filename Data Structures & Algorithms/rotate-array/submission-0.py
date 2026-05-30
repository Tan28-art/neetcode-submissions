class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def rotate_array():    
            last = nums.pop()
            nums.insert(0, last)

        for i in range(k):
            rotate_array()
            
