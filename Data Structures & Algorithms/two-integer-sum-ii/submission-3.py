class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        h = 0
        t = len(numbers) - 1
        s = 0

        while h < t:
            s = numbers[h] + numbers[t]
            if s == target:
                return [h+1, t+1]
            if s < target:
                h += 1
            else:
                t -= 1
        return []
        