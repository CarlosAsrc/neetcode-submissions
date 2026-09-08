class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        last_cs = {}
        
        for r in range(len(s)):
            if s[r] in last_cs:
                l = max(last_cs[s[r]] + 1, l)
            last_cs[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest


        