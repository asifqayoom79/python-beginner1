def square(x):
    return x**2
numbers = (input("enter a list of integers:")).split()
numbers =list(map(int, numbers))
square_num = list(map(square,numbers))
print("original numbers are:",numbers)
print("tripled numbers are:", square_num)