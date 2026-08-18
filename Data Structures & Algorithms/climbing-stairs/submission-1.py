class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(n, total) -> int:
            if total == n:
                return 1
            if total > n:
                return 0
            
            if cache[total] != -1:
                return cache[total]
            cache[total] = dfs(n, total + 1) + dfs(n, total + 2)

            return cache[total]
        
        return dfs(n, 0)
    
