def calculate_max_removals(main_str, substrings, memo):
    # Check if the result for the current string is already computed
    if main_str in memo:
        return memo[main_str]

    max_removals = 0

    # Iterate through each substring in the list
    for substring in substrings:
        pos = main_str.find(substring)
        if pos != -1:
            # Create a new string by removing the found substring
            modified_str = main_str[:pos] + main_str[pos + len(substring):]
            # Recursively calculate the max removals
            max_removals = max(max_removals, 1 + calculate_max_removals(modified_str, substrings, memo))

    memo[main_str] = max_removals
    return max_removals


if __name__ == "__main__":
    num_substrings = int(input())
    substrings = input().split()
    main_str = input().strip()

    memo = {}
    print(calculate_max_removals(main_str, substrings, memo))
