def precedence(operator):
    precedence_map = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedence_map.get(operator, 0)

def infix_to_postfix(expression):
    stack = []
    postfix = []
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix.append(stack.pop())
            stack.append(char)
    
    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)

# Example usage
infix_expression = "a+b*(c^d-e)^(f+g*h)-i"
print("Infix expression:", infix_expression)
print("Postfix expression:", infix_to_postfix(infix_expression))
