def rabin_karp(text, pattern):
    ans = []
    n = len(text)
    k = len(pattern)

    base = 256  # total ascii of valid chars
    prime = 101

    textHash = 0
    patternHash = 0
    h = 1

    # determining h
    for _ in range(k-1):
        h = (h*base) % prime

    # determining th patternHash and initial window textHash
    for i in range(k):
        patternHash = (patternHash * base + ord(pattern[i]) ) % prime
        textHash = ( textHash * base + ord(text[i]) ) % prime

    # sliding window - rotating Hash
    left = 0
    right = k-1


    while right < n:

        if textHash == patternHash:
            # there might be cases where hash value will still be equal for different stirngs
            if text[left:right+1] == pattern:
                ans.append(left)

        if right < n-1:
            textHash = (textHash - (h * ord(text[left])) % prime) % prime     # removed left val
            textHash = ( (textHash * base) + ord(text[right + 1])) % prime        # added right val

        left += 1
        right += 1

    return ans


if __name__ == '__main__':
    text = input("Enter the string : ")
    pattern = input("Enter the pattern : ")

    res = rabin_karp(text, pattern)
    print(res)
