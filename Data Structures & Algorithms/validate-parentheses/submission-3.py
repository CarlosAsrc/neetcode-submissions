class Solution:
    def isValid(self, s: str) -> bool:
        symbols = {
            '(': 1,
            ')': -1,
            '{': 2,
            '}': -2,
            '[': 3,
            ']': -3
        }
        stack = []
        stack.append(s[0])
        count = symbols[s[0]]
        for x in s[1:]:
            print(stack)
            if len(stack)>0 and symbols[stack[-1]] + symbols[x] == 0:
                count+=symbols[x]
                print(count)
                stack.pop()
            else:
                count+=symbols[x]
                print(count)
                if count < 0:
                    return False
                stack.append(x)
        if len(stack) == 0:
            return True
        return False
        