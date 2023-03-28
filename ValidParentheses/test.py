def isValid(s: str) -> bool:
        stack = []

        left_set = set('([{')
        right_set = set(')]}')

        parentheses_dictionary = {
        '[': ']',
        '(': ')',
        '{': '}'
    }

        for char in s:
            if char in left_set:
                stack.append(char)
            if char in right_set:
                print(char)
                print(stack[-1])
                if not stack:
                    return False
                elif char == parentheses_dictionary[stack[-1]]:
                    print(stack[-1])
                    stack.pop()
        return stack == []

print(isValid('{}'))