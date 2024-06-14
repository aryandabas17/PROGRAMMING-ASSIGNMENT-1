def fib(n):
    if n <= 0:
        return "Input should be a positive integer."
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


a = int(input("How many numbers you wish to print in Fibonacci sequence : \n"))
for i in range(0, a+1):
    print(fib(i))