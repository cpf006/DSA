# https://leetcode.com/problems/valid-parentheses/description/
# My first solution
class Solution:
    def isValid(self, s: str) -> bool:
        rounded = []
        square = []
        curly = []
        currentType = ''
        openings = '([{'
    
        for char in s:
            if currentType != '':
                if (
                    currentType == '(' and char in ']}' or
                    currentType == '[' and char in ')}' or
                    currentType == '{' and char in ')]'
                ):
                    return False

            if char == '(' or char == ')':
                currentType = '('
                rounded = self.adjustStack(char, rounded)
                if len(rounded) == 0:
                    currentType = ''
            elif char == '[' or char == ']':
                currentType = '['
                square = self.adjustStack(char, square)
                if len(square) == 0:
                    currentType = ''
            else:
                currentType = '{'
                curly = self.adjustStack(char, curly)
                if len(curly) == 0:
                    currentType = ''

        return len(rounded) == len(square) == len(curly) == 0
    
    def adjustStack(self, char: str, stack: list):
        openings = '([{'
        closings = ')}]'

        if len(stack):
            last = stack.pop()
            if last == char or char not in closings:
                stack.append(last)
                stack.append(char)
        else:
            stack.append(char)
        
        return stack

'''
Think stack to track order of parentheses and dictionary to determine if its a match
'''


# After looking at a solution and coming back to it:

class Solution:
    def isValid(self, s: str) -> bool:
        openingsToClosings = {
            '(':')',
            '{':'}',
            '[':']',
        }
        stack = []
    
        for char in s:
            if char in "({[":
                stack.append(char)
            elif len(stack) and openingsToClosings[stack.pop()] == char:
                continue
            else:
                return False
                
        return len(stack) == 0
        