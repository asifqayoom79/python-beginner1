def triple(x):
    return x*3
numbers = (input("enter a list of integers:")).split()
numbers =list(map(int, numbers))
triple_num = list(map(triple,numbers))
print("original numbers are:",numbers)
print("tripled numbers are:", triple_num)


