class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(index, subset, total):
            if total == target:
                result.append(subset.copy())
                return
            elif (total > target) or (index >= len(nums)):
                return

            #include nums[index]
            subset.append(nums[index])
            dfs(index, subset, total + nums[index])

            #dont include nums[index]
            subset.pop()
            dfs(index + 1, subset, total)

        dfs(0, [], 0)
        return result


            