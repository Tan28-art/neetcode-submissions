class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the given array
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            left = i
            right = n-1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if i == left:
                    left += 1
                elif i == right:
                    right -= 1
                elif sum == 0:
                    if [nums[i], nums[left], nums[right]] not in result:
                        result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
                
    