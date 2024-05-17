class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def construct_expression_tree(postfix_expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    for token in postfix_expression:
        if token in operators:
            node = Node(token)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
        else:
            stack.append(Node(token))

    return stack.pop()

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Example usage
postfix_expression = "ab+ef*g*-"
root = construct_expression_tree(postfix_expression)
print("Inorder traversal of the expression tree:")
inorder_traversal(root)
