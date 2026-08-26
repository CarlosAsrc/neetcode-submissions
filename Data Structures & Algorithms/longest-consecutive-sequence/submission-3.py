class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 1

        if len(nums) < 2:
            return len(nums)

        for n in nums:
            length = 1
            if n-1 not in nums:
                while n+length in nums:
                    length+=1
                    longest = max(length, longest)
        return longest
                
