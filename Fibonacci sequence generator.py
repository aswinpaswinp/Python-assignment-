# Function to generate Fibonacci sequence up to n terms
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Input from the user
n = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence and print it
fib_sequence = fibonacci(n)
print(", ".join(map(str, fib_sequence)))
