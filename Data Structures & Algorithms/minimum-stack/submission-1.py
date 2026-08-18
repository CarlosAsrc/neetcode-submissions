class MinStack:

    def __init__(self):
        self.minStack = []
        self.minElements = []
        

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if len(self.minElements) == 0 or self.minElements[-1] >= val:
            self.minElements.append(val)
        

    def pop(self) -> None:
        if self.minStack[-1] == self.minElements[-1]:
            self.minElements.pop()
        self.minStack.pop()
            
        

    def top(self) -> int:
        return self.minStack[-1]
        

    def getMin(self) -> int:
        return self.minElements[-1]
