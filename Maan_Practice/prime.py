def is_prime(num):
    # Numbers less than 2 are not prime
    if num < 2:
        return False
    
    # Check for divisibility from 2 to square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

# Test the function
number = int(input("Enter a number to check if it's prime: "))
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")