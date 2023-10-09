def validate(s):
    """Validate that a given square is valid."""
    
    # Base case: If s is a number, it must be either 0 or 1.
    if isinstance(s, int):
        return s in [0, 1]

    # If s is a list, it must contain exactly four items.
    if isinstance(s, list) and len(s) == 4:
        # Recursively validate each element of the list.
        return all(validate(subsquare) for subsquare in s)
    
    # If neither of the above conditions is met, s is not valid.
    return False

# Example tests
if __name__ == "__main__":
    s1 = 0
    print(validate(s1))  # Output: True

    s2 = [1, 1, 1, 1]
    print(validate(s2))  # Output: True

    s3 = [1, 0, [1, [0, 0, 0, 0], 1, [1, 1, 1, 1]], 1]
    print(validate(s3))  # Output: True

    s4 = 2
    print(validate(s4))  # Output: False

    s5 = [1, 1, 1, 1, 1]
    print(validate(s5))  # Output: False

    s6 = [1, 0, [1, [0, 0, 0, 0, 1], 1, [1, 1, 1, 1]], 1]
    print(validate(s6))  # Output: False

    s7 = [1, [1, 0, 1, [0, [0, 0, 0], 1, 1]], [1, 0, 1, 0], 1]
    print(validate(s7))  # Output: False
