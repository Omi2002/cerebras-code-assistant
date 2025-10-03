# **Prime Check Function**
# ========================

# The following function checks if a given number is prime or not. It will return `True` if the number is prime and `False` otherwise.

# ```python
# def is_prime(n):
#     """
#     Checks if a number is prime.

#     Args:
#     n (int): The number to check.

#     Returns:
#     bool: True if the number is prime, False otherwise.

#     Raises:
#     TypeError: If n is not an integer.
#     ValueError: If n is less than 2.
#     """
#     if not isinstance(n, int):
#         raise TypeError("Input must be an integer.")
#     if n < 2:
#         raise ValueError("Input must be a positive integer.")

#     # Check if the number is divisible by any number up to its square root
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False

#     # If the number is not divisible by any number up to its square root, it's prime
#     return True
# ```

# **Example Use Cases**
# ---------------------

# ```python
# # Test the function with some examples
# print(is_prime(25))  # False
# print(is_prime(23))  # True
# print(is_prime(37))  # True
# print(is_prime(48))  # False

# # Test the function's error handling
# try:
#     print(is_prime(1.5))  # Raises TypeError
# except TypeError as e:
#     print(e)

# try:
#     print(is_prime(-5))  # Raises ValueError
# except ValueError as e:
#     print(e)
# ```

# This function uses a simple trial division method, where it checks if the number is divisible by any number up to its square root. This is an efficient method for checking primality, as it eliminates the need to check all the way up to the number itself.