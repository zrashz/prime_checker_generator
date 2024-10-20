"""
Prime number checker and generator.

This module provides a menu-driven program to check if a number is prime and to generate
a list of prime numbers within a specified range.
"""

# Function to check if a number is prime
def is_prime(num):
    """
    Check if a number is prime.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Only check up to the square root of num
        if num % i == 0:
            return False
    return True

# Function to generate all prime numbers in a given range
def generate_primes(start, end):
    """
    Generate all prime numbers in a given range.

    Args:
    start (int): The starting number of the range.
    end (int): The ending number of the range.

    Returns:
    list: A list of prime numbers within the range.
    """
    prime_list = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

# Main program
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Check if a number is prime")
        print("2. Generate prime numbers in a range")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            # Prime checker
            number = int(input("Enter a number to check: "))
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")

        elif choice == '2':
            # Prime number generator
            start_range = int(input("Enter the start of the range: "))
            end_range = int(input("Enter the end of the range: "))
            primes = generate_primes(start_range, end_range)
            print(f"Prime numbers between {start_range} and {end_range}:")
            print(primes)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
