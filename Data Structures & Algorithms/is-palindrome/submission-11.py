class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        h = 0
        t = len(s) - 1

        while h < t:
            if s[h] != s[t]:
                return False
            h+=1
            t-=1
        return True 
        