class Solution:
    def isValid(self, s: str) -> bool:
 
        table = {
            '[' : ']',
            '(' : ')',
            '{' : '}'
        }

        stack = []
        for char in s:
            if char in table:
                stack.append(char)
            elif not stack or table[stack.pop()] != char:
                return False 
        
        return len(stack) == 0
            
                



s = Solution()

a = "[]"

s.isValid(a)