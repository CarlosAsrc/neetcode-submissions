class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = len(nums)//2
        while i >= 0 and i < len(nums):
            if nums[i] == target:
                return i
            if nums[i] < target and i >= len(nums)//2:
                i+=1
            else:
                if i <= len(nums)//2:
                    i-=1
                else:
                    return -1
        return -1

        