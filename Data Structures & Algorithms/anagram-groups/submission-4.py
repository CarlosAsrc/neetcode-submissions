class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            frequency = [0] * 26
            for l in s:
                frequency[ord(l) - ord('a')] = frequency[ord(l) - ord('a')] + 1
            if tuple(frequency) in seen:
                seen[tuple(frequency)].append(s)
            else:
                seen[tuple(frequency)] = [s]
        return list(seen.values())

        
        