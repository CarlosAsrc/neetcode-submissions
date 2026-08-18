class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(n):
            if n >= len(nums):
                result.append(subset[::])
                return
            
            subset.append(nums[n])
            backtrack(n+1)
            
            subset.pop()
            backtrack(n+1)
        backtrack(0)
        return result

        
        
