def isValid(s: str) -> bool:

    table = {
        '[': ']',
        '(': ')',
        '{': '}'
    }

    stack = []

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[stack.pop()] != char:
            return False
        
    return len(stack) == 0


print(isValid('{}'))