class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        s = [x.lower() for x in s if x.isalnum()]
        
        if len(s) == 2:
            return s[0].lower() == s[1].lower()

        i = 0
        j = len(s)-1

        while i<j:
            if not s[i]:
                i+=1
                continue
            if not s[j]:
                j-=1
                continue
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True
            

        