class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            count[n] = 0
        for n in nums:
            count[n] = count[n] + 1
        for i, v in count.items():
            if v > 1:
                return True
        return False