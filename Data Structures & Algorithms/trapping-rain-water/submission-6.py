class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0

        l = 0
        l_max = 0
        r = len(height)-1
        r_max = len(height)-1

        while (l < r):
            if height[l] < height[r]:
                l = l+1
                if height[l] < height[l_max]:
                    volume += height[l_max] - height[l]
                else:
                    l_max = l
            else:
                r = r-1
                if height[r] < height[r_max]:
                    volume += height[r_max] - height[r]
                else:
                    r_max = r
        return volume
        
        

    

        