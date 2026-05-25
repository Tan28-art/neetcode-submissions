class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # two decisions: to include or not to include
        result = []
        subset = []

        def dfs(index):
            if index >= len(nums):
                result.append(subset.copy())
                return
            
            # to include 
            subset.append(nums[index])
            dfs(index + 1)

            # not to include
            subset.pop()
            dfs(index + 1)

            

        dfs(0)
        return result