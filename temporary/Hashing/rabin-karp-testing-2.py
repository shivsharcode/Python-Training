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
        right = k  # 1 value ahead of the window

        print("Patternhash = ", patternHash)
        print()

        while right < n:
            # print(f"window = {text[left:right]}")
            print("TextHash = ", textHash)
            if patternHash == textHash:
                ans.append(left + 1)
                print(f"window = {text[left:right]}, index = {left+1}")


            textHash = (textHash - (h * ord(text[left])) % prime) % prime  # removed left val
            textHash = (textHash * base + ord(text[right])) % prime  # added the right val

            left += 1
            right += 1

        return ans


if __name__ == "__main__":
    text = input("Enter textstr : ")
    pattern = input("Enter pattern string : ")

    solution = Solution()
    res = solution.search(pattern, text)
    print(res)
