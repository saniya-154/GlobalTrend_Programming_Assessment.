#Write a Python function to compute the nth Fibonacci number using recursion.
def fibonacci(n):
    if n <= 0:
        raise ValueError("Input should be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


try:
    n = int(input("Enter a number:")) # Change this value to compute a different Fibonacci number
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
except ValueError as ve:
    print(ve)