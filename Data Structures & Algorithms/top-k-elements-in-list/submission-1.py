class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for n in nums:
            if n in frequency:
                frequency[n] += 1
            else:
                frequency[n] = 1
        sorted_keys = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_keys)[:k]