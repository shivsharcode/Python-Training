# COMPLEXITY : O(n * k^2) ; n = length  of string, k = length of pattern
def pattern_matching_testing(s, pattern):
    ans = []
    it = 0
    n = len(s)
    k = len(pattern)

    for i in range(n):     # O(n)
        j = i
        sub = ""
        while it < k and s[j] == pattern[it]:   # O(k)
            sub += s[j]     # string concatenation # O(k)
            j += 1
            it += 1

        if sub == pattern:
            ans.append((i, sub))

        it = 0
    return ans


if __name__ == '__main__':
    s = input("Enter string : ")
    pattern = input("Enter pattern")

    result = pattern_matching_testing(s, pattern)
    print(result)
