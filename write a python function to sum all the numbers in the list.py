def sum_numbers(num):
    total = 0
    for i in num:
        total += i
    return total
numbers_list = [1, 2, 3, 4, 5]
result = sum_numbers(numbers_list)
print("Sum of numbers:", result)