# write a python program to count the number of even and odd numbers from a series of numbers.
def count_odd_even(numbers):
    odd_count = 0
    even_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return odd_count, even_count


series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd, even = count_odd_even(series)

print("Number of odd numbers:", odd)
print("Number of even numbers:", even)

