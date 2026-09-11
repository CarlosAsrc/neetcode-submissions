class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_frequency = [0] * 26
        for c in s1:
            s1_frequency[ord(c)-ord('a')] += 1
        
        l, r = 0, 0
        s2_frequency = [0] * 26

        while r < len(s2):
            if r - l < len(s1):
                s2_frequency[ord(s2[r])-ord('a')] += 1
                r += 1
            else:
                s2_frequency[ord(s2[r])-ord('a')] += 1
                r += 1
                s2_frequency[ord(s2[l])-ord('a')] -= 1
                s2_frequency[ord(s2[l])-ord('a')] = max(s2_frequency[ord(s2[l])-ord('a')], 0)
                l += 1
            print(s1_frequency)
            print(s2_frequency)
            print('/n')
            if s2_frequency == s1_frequency:
                return True
        return False

        

        
        