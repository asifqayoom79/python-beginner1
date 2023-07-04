def sum_numbers(list1):
    total = sum(list1)
    return total
list1 = list(map(int,input("enter the list:").split()))
result = sum_numbers(list1)
print("Sum of numbers:", result)
