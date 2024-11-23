# Complexity : O(n-k+1)(2k)  ==> O(n*k)
def pattern_matching_testing2(s,  pattern):
    ans = []
    n = len(s)
    k = len(pattern)

    left = 0
    right = k-1

    while right < n:            # O(n-k+1)
        sub = s[left:right+1]   # O(k)
        if sub == pattern:      # O(k)
            ans.append((left, sub))

        left += 1
        right += 1

    return ans


if __name__ == '__main__':
    s = input("Enter string : ")
    pattern = input("Enter pattern : ")

    result = pattern_matching_testing2(s, pattern)
    print(result)
