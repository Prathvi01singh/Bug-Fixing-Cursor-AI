"""Project 3: Bug Fixing
A buggy program, the explanation, and the corrected version with tests.

---------- BUGGY VERSION ----------
    def sum_list(numbers):
        total = 0
        for i in range(len(numbers) + 1):   # BUG 1: goes one index too far -> IndexError
            total += numbers[i]
        return total

    def find_max(numbers):
        maximum = 0                          # BUG 2: wrong for all-negative lists
        for n in numbers:
            if n > maximum:
                maximum = n
        return maximum

---------- FIXED VERSION (below) ----------
"""


def sum_list(numbers):
    total = 0
    for n in numbers:            # FIX 1: loop over the items directly
        total += n
    return total


def find_max(numbers):
    if not numbers:
        raise ValueError("find_max needs at least one number.")
    maximum = numbers[0]         # FIX 2: start from the first element
    for n in numbers[1:]:
        if n > maximum:
            maximum = n
    return maximum


def main():
    # Tests that fail on the buggy version and pass on the fixed one
    assert sum_list([1, 2, 3, 4]) == 10
    assert find_max([-8, -3, -15]) == -3
    assert find_max([4, 9, 2]) == 9

    print("Sum of [1, 2, 3, 4]:", sum_list([1, 2, 3, 4]))
    print("Max of [-8, -3, -15]:", find_max([-8, -3, -15]))
    print("All tests passed.")


if __name__ == "__main__":
    main()
