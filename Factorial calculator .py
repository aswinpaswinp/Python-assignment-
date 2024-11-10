# Function to compute factorial using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Function to compute factorial using iteration
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Input: Get a number from the user
num = int(input("Enter a number to compute its factorial: "))

# Compute factorial using recursion and iteration
fact_recursive = factorial_recursive(num)
fact_iterative = factorial_iterative(num)

# Output the results
print(f"Factorial of {num} using recursion is: {fact_rec
