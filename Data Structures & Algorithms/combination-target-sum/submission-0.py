class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def backtracking(i, total):
            if total == target:
                result.append(subset[::])
                return
            
            if i >= len(nums) or total > target:
                return
            
            subset.append(nums[i])
            backtracking(i, total + nums[i])

            subset.pop()
            backtracking(i+1, total)
        backtracking(0, 0)
        return result
        