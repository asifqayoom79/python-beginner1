#4. Q4. Write a program to print the first non-repeated character from a string?
def first_non_repeated_character(s):
    char_freq = {}
    
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    for char in s:
        if char_freq[char] == 1:
            return char
    
    return None

if __name__ == "__main__":
    input_string = "ebcbed"
    result = first_non_repeated_character(input_string)
    
    if result is not None:
        print("The first non-repeated character is:", result)
    else:
        print("There is no non-repeated character in the string.")

#5. Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it?
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("\n"f"Move disk 1 from {source} to {destination}")
        return
    
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)

if __name__ == "__main__":
    num_disks = 3
    tower_of_hanoi(num_disks, 'A', 'B', 'C')


#6.Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
def is_operator(char):
    return char in "+-*/^"

def postfix_to_prefix(postfix_expression):
    stack = []
    for char in postfix_expression.split():
        if not is_operator(char):
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            expression = char + " " + operand1 + " " + operand2
            stack.append(expression)
    return stack.pop()
postfix_expression = "3 4 +"
prefix_expression = postfix_to_prefix(postfix_expression)
print("\nPostfix Expression:", postfix_expression)
print("Prefix Expression:", prefix_expression)
