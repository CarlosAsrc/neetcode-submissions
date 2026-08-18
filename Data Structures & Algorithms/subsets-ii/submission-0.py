class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        subset = []

        def backtrack(i):
            if i >= len(nums):
                result.add(tuple(subset[:]))
                return
            
            subset.append(nums[i])
            backtrack(i+1)
            
            subset.pop()
            backtrack(i+1)
        nums.sort()
        backtrack(0)
        return [list(l) for l in result]
        