import math

def calculate_hypotenuse(a, b):
    """
    Calculates the length of the hypotenuse (c) using the Pythagorean theorem.
    Args:
        a (float): Length of side 'a'.
        b (float): Length of side 'b'.
    Returns:
        float: Length of the hypotenuse 'c'.
    """
    return math.sqrt(a ** 2 + b ** 2)

# Example usage:
# a = 3
# b = 4
# hypotenuse = calculate_hypotenuse(a, b)
# print(f"The length of the hypotenuse c is {hypotenuse:.2f}")


# Determine if a given number is a prime number
def is_prime(num):
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    for i in range(2, num):
        if (num % i) == 0:
            return False  # If factor is found, it's not prime

    return True  # Otherwise, it's prime
