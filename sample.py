"""Simple sample Python script.

This script calculates the factorial of a number and prints the result.
"""


def factorial(n: int) -> int:
    """Return n! for non-negative integer n."""
    if n < 0:
        raise ValueError("n must be non-negative")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    number = 5
    print(f"Factorial of {number} is {factorial(number)}")
