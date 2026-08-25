class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for n in nums:
            product *= n
        
        products = [product] * len(nums)
        res = [0] * len(nums)

        for i, n in enumerate(nums):
            if n == 0:
                product2 = 1
                for j, x in enumerate(nums):
                    if i != j:
                        product2 *= x
                res[i] = product2
            else:    
                res[i] = product // n
        return res


        