# test 3.py

"""Compute the average of a list of numbers."""

from typing import List


def average(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Cannot compute average of an empty list")
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    sample_numbers = [10, 20, 30, 40, 50]
    print(f"Numbers: {sample_numbers}")
    print(f"Average: {average(sample_numbers)}")
