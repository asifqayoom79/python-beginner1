def fibonacci_series(start, end):
    series = [0, 1]  
    fib_num = 1  

    while fib_num <= end:
        next_num = series[-1] + series[-2]  
        series.append(next_num)  
        fib_num = next_num  


    series = [num for num in series if num >= start and num <= end]

    return series

fib_series = fibonacci_series(0, 50)

for num in fib_series:
    print(num, end=" ")

