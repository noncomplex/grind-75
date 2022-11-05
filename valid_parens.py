# append proper opening brackets in a stack representation
# if char is not opening bracket check to see if it closes
# last open
# else false
# if empty return True
# O(n)

def isValid(self, s: str) -> bool:
    stack = []
    types = {'(':')', '{':'}', '[':']'}
    for char in s:
        if char in types:
            stack.append(char)
        elif stack and char == types[stack[-1]]:
            stack.pop()
        else:
            return False
    return not(bool(stack))
