def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find and return all prime numbers in a given range [start, end]."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Get user input for the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Find and print all primes in the given range
primes = find_primes_in_range(start, end)
print(f"Prime numbers in the range {start} to {end} are: {primes}")
