class MinStack:

    def __init__(self):
        #we can define 2 stacks, one for values and one for minimun values 
        self.stack = []
        self.minvalues= []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_value= min(val, self.minvalues[-1] if self.minvalues else val)
        self.minvalues.append(min_value)

    def pop(self) -> None:
        #we need to remove it from bot
        self.stack.pop()
        self.minvalues.pop() 


    def top(self) -> int:
        return self.stack[-1] 

    def getMin(self) -> int:
        
        return self.minvalues[-1]

