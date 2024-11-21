class Solution:
    def search(self, pattern, text):
        n = len(text)
        k = len(pattern)
        base = 26
        prime = 101

        textHash = 0
        patternHash = 0
        h = 1

        for _ in range(k - 1):
            h = (h * base) % prime

        # Calculate initial hash values
        for i in range(k):
            patternHash = (patternHash * base + ord(pattern[i])) % prime
            textHash = (textHash * base + ord(text[i])) % prime

        ans = []
        left = 0
        right = k

        while right < n:
            if patternHash == textHash:
                # there might be cases where still the hash values get equal so for prevention
                if text[left:right] == pattern:
                    ans.append(left + 1)

            textHash = (textHash - (h * ord(text[left])) % prime) % prime
            textHash = (textHash * base + ord(text[right])) % prime

            left += 1
            right += 1

        return ans


if __name__ == "__main__":
    text = input("Enter textstr : ")
    pattern = input("Enter pattern string : ")

    solution = Solution()
    res = solution.search(pattern, text)
    print(res)
