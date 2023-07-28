#7.  Write a program to convert prefix expression to infix expression.
def is_operator(char):
    return char in "+-*/^"

def prefix_to_infix(prefix_expression):
    stack = []
    for char in reversed(prefix_expression.split()):
        if not is_operator(char):
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            expression = "(" + operand1 + " " + char + " " + operand2 + ")"
            stack.append(expression)
    return stack.pop()

prefix_expression = "+ 3 4"
infix_expression = prefix_to_infix(prefix_expression)
print("Prefix Expression:", prefix_expression)
print("Infix Expression:", infix_expression)

#8. Write a program to check if all the brackets are closed in a given code snippet.
def are_brackets_balanced(code_snippet):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in code_snippet:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return False  
            last_opening_bracket = stack.pop()
            if bracket_pairs[char] != last_opening_bracket:
                return False  

    return len(stack) == 0  

code_snippet = "{(a + b) * [c - d]}"
if are_brackets_balanced(code_snippet):
    print("\nAll brackets are closed properly.")
else:
    print("Bracket mismatch found.")


#9. Write a program to reverse a stack?
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)


def reverse_stack(stack):
    auxiliary_stack = Stack()

    
    while not stack.is_empty():
        auxiliary_stack.push(stack.pop())

    while not auxiliary_stack.is_empty():
        stack.push(auxiliary_stack.pop())


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)

    print("\nOriginal Stack:", my_stack.items)
    reverse_stack(my_stack)
    print("Reversed Stack:", my_stack.items)

#10. 
class Stack:
    def __init__(self):
        self.items = []
        self.min_element = None

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.is_empty() or item < self.min_element:
            self.min_element = item
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def get_min(self):
        return self.min_element


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(5)
    my_stack.push(2)
    my_stack.push(8)
    my_stack.push(1)

    print("\nStack elements:", my_stack.items)
    print("Smallest number:", my_stack.get_min())

