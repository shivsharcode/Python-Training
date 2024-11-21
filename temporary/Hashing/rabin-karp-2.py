class Solution:
    def search(self, pattern, text):
        ans = []
        n = len(text)
        k = len(pattern)
        base = 26
        prime = 101

        textHash = 0
        patternHash = 0
        h = 1

        for _ in range(k - 1):
            h = (h * base) % prime

        # calculating initial hash values for the pattern and the first window of the text
        for i in range(k):
            patternHash = (patternHash * base + ord(pattern[i])) % prime
            textHash = (textHash * base + ord(text[i])) % prime

        # sliding window (rolling hash)
        left = 0
        right = k - 1  # 1 value ahead of the window

        while right < n:
            if patternHash == textHash:
                if text[left:right + 1] == pattern:
                    ans.append(left + 1)

            if right < n - 1:
                textHash = (textHash - (h * ord(text[left])) % prime) % prime  # removed left val
                textHash = (textHash * base + ord(text[right + 1])) % prime  # added the next right val

            left += 1
            right += 1

        return ans


if __name__ == '__main__':
    text = input("Enter the string : ")
    pattern = input("Enter the pattern : ")
    solution = Solution()

    res = solution.search( pattern, text)
    print(res)