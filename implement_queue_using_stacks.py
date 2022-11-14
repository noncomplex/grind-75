# key is that a stack reversed can easily function as a queue
# push to 1 stack
# and add the reverse to another
# stack 2 must be empty before being added to because
# if not there would be previous elements that need to be popped
# first
# note: using lists to represent stacks and [-1] index for stack peep

class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, x: int) -> None:
        self.s1.append(x)
        
    def pop(self) -> int:
        if self.s2:
            return self.s2.pop()
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
        

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        else:
            return self.s1[0]
        
    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0
