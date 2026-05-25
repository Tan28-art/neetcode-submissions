class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        final_left = 0
        final_right = 0
        sum = 10000

        while sum != target:
            sum = numbers[left] + numbers[right]

            if sum > target:
                right -= 1
            
            elif sum < target:
                left += 1

            else:
                final_left = left + 1
                final_right = right + 1

        return [final_left, final_right]