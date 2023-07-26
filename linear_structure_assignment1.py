#6. Find the Kth largest and Kth smallest number in an array
def find_kth_largest_smallest(arr, k):
    if k > len(arr) or k < 1:
        return None

    arr.sort()
    kth_smallest = arr[k - 1]
    kth_largest = arr[-k]
    return kth_largest, kth_smallest

if __name__ == "__main__":
    arr = [3, 7, 1, 9, 4, 6, 8, 2, 5]
    k = 3
    kth_largest, kth_smallest = find_kth_largest_smallest(arr, k)
    print(f"{k}th largest number in the array:", kth_largest)
    print(f"{k}th smallest number in the array:", kth_smallest)

#7.  Move all the negative elements to one side of the array
def move_negatives_to_one_side(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] >= 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] >= 0 and arr[right] >= 0:
            right -= 1
        else:
            left += 1
            right -= 1
    return arr

if __name__ == "__main__":
    arr = [1, -2, 3, -4, -5, 6, -7, -8, 9]
    print("Original Array:", arr)

    arr = move_negatives_to_one_side(arr)

    print("\nArray after moving negatives to one side:", arr)


#8 Reverse a string using a stack data structure
def reverse_string_using_stack(s):
    stack = []
    for char in s:
        stack.append(char)

    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string

if __name__ == "__main__":
    input_string = "Hello, World!"
    print("\nOriginal String:", input_string)

    reversed_string = reverse_string_using_stack(input_string)
    print("Reversed String:", reversed_string)


#9. Evaluate a postfix expression using stack
def evaluate_postfix_expression(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)

    return stack.pop()

if __name__ == "__main__":
    postfix_expression = "34+2*"
    result = evaluate_postfix_expression(postfix_expression)
    print("\nResult of the postfix expression:", result)


#10, Implement a queue using the stack data structure
class QueueUsingStack:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, val):
        self.in_stack.append(val)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("Queue is empty")
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("Queue is empty")
        return self.out_stack[-1]

    def is_empty(self):
        return not self.in_stack and not self.out_stack

if __name__ == "__main__":
    queue = QueueUsingStack()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("\nPeek:", queue.peek())  

    print("Dequeue:", queue.dequeue()) 

    queue.enqueue(4)

    print("Dequeue:", queue.dequeue()) 

    print("Is Queue Empty?", queue.is_empty()) 

    print("Dequeue:", queue.dequeue())  

    print("Is Queue Empty?", queue.is_empty())  

    print("Dequeue:", queue.dequeue())  

    print("Is Queue Empty?", queue.is_empty()) 


    try:
        print("Dequeue:", queue.dequeue())
    except IndexError as e:
        print("Error:", e)  # Output: Error: Queue is empty

