class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort() # nlogn

        for i in range(len(nums) - 1):

            if nums[i] > 0:
                break

            if i > 0 and (nums[i] == nums[i-1]):
                continue

            number1 = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[left] + nums[right] + number1

                if sum > 0:
                    right -= 1

                elif sum < 0:
                    left += 1
                
                else:
                    number2 = nums[left]
                    number3 = nums[right]
                    answer.append([number1, number2, number3])
                    left += 1
                    right -= 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                [-4,-1,-1,0,1,2]
        
        return answer