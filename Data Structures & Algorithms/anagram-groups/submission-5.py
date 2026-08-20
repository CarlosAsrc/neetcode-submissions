class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            frequency = [0] * 26
            for l in s:
                frequency[ord(l) - ord('a')] = frequency[ord(l) - ord('a')] + 1
            key = tuple(frequency)
            if key in seen:
                seen[key].append(s)
            else:
                seen[key] = [s]
        return list(seen.values())

        
        