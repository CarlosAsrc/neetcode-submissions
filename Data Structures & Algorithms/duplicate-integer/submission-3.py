class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for i, n in enumerate(nums):
            if n not in seen:
                seen.add(n)
            else:
                return True
        return False
        