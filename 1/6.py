# function to check if a number is prime or not 
def is_prime(a):
    if a <= 1:
        return False
    for j in range(2, int(a**0.5) + 1):
        if a % j == 0:
            return False
    return True

#  Take range 
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Find prime number
primes = [num for num in range(start, end + 1) if is_prime(num)]

# Display output
print(f"Prime numbers in the range {start} to {end}: {primes}")
print(f"Count of prime numbers: {len(primes)}")
print(f"Sum of prime numbers: {sum(primes)}")