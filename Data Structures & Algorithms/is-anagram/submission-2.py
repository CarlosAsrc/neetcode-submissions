class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ocurrencies_s = self.get_ocurrencies(s)
        ocurrencies_t = self.get_ocurrencies(t)
        return ocurrencies_s == ocurrencies_t
        
        
    def get_ocurrencies(self, s) -> {}:
        seen = {}
        for l in s:
            if l not in seen:
                seen[l] = 1
            else:
                seen[l] = seen[l]+1
        return seen


        