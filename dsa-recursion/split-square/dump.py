def dump(s, indent=0):
    """Print each square on a new line with proper indentation."""
    
    # Base case: If s is a number, print it with proper indentation.
    if isinstance(s, int):
        print(" " * indent + str(s))
    
    # If s is a list, iterate through its elements.
    elif isinstance(s, list):
        for item in s:
            # Recursively print each element with increased indentation.
            dump(item, indent + 1)

# Example tests
if __name__ == "__main__":
    s1 = 0
    dump(s1)  # Output: 0

    s2 = 1
    dump(s2)  # Output: 1

    s3 = [0, 1, 0, 1]
    dump(s3)
    # Output:
    # 0
    # 1
    # 0
    # 1

    s4 = [0, 0, 0, [1, 1, 1, 1]]
    dump(s4)
    # Output:
    # 0
    # 0
    # 0
    # 1
    # 1
    # 1
    # 1

    s5 = [0, 0, 0, [1, 1, 1, [0, 0, 0, [1, 1, 1, 1]]]]
    dump(s5)
    # Output:
    # 0
    # 0
    # 0
    # 1
    # 1
    # 1
    # 0
    # 0
    # 0
    # 1
    # 1
    # 1
    # 1
