class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1

            while j < k:
                s = -(nums[j] + nums[k])
                    
                if nums[i] == s:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                if nums[i] > s:
                    k-=1
                else:
                    j+=1
        
        return res

