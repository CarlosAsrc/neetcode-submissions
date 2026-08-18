class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        c = {}

        z = sorted(zip(startTime, endTime, profit))

        def backtrack(i):
            if i >= len(z):
                return 0
            if i in c:
                return c[i]
            
            total = backtrack(i+1)

            j = i+1
            while j < len(z):
                if z[i][1] <= z[j][0]:
                    break
                j+=1
            total = max(total, z[i][2] + backtrack(j))
            c[i] = total
            return total

        return backtrack(0)
        
        
            
            

