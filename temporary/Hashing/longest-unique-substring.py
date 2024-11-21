
def longest_unique_substring_length(s):
    char_set = set()
    left = 0
    maxLength = 0

    for right in range(len(s)):
        # if duplicate character, move left pointer to maintain unique chars
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # add current char to set and update marks if needed
        char_set.add(s[right])
        maxLength = max(maxLength, right - left + 1)

    return maxLength


if __name__ == '__main__':
    s = input("Enter string : ")
    max_length = longest_unique_substring_length(s)
    print(max_length)
