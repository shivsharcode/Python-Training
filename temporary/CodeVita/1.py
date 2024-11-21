def invalidInput(s):
    for i in s:
        if i != '0' and i != '1':
            print("INVALID", end="")
            return True

    return False


def costCalculator(s, a, b):
    i = 0
    # j = 1

    freq01, freq10 = 0, 0

    while i < len(s) - 1:
        if s[i] + s[i + 1] == '01':
            freq01 += 1
        elif s[i] + s[i + 1] == '10':
            freq10 += 1
        i += 1

    totalCost = a * freq01 + b * freq10
    return totalCost


def reArrange(orgStr, a, b):
    # which is smaller a or b
    if a > b:
        lowCostSeq = '10'
    else:
        lowCostSeq = '01'

    # newArr = [0]*len(orgStr)
    onesCount = orgStr.count('1')
    zeroCount = orgStr.count('0')

    newStr = ""
    if lowCostSeq == '10':
        newStr = '1' * onesCount + '0' * zeroCount
    else:
        newStr = '0' * zeroCount + '1' * onesCount

    return newStr


def hammingDistance(orgStr, newStr):
    hd = 0
    for i, j in zip(orgStr, newStr):
        if i != j:
            hd += 1

    return hd


t = int(input())  # testcases
# solution=list()

while t:
    orgStr = input()
    a, b = map(int, input().split())

    isInvalidInput = invalidInput(orgStr)

    if not isInvalidInput:
        orgCost = costCalculator(orgStr, a, b)
        reArrangedStr = reArrange(orgStr, a, b)
        newCost = costCalculator(reArrangedStr, a, b)

        hd = hammingDistance(orgStr, reArrangedStr)
        print(hd)

    t -= 1

'''for i in solution:
  print(i)'''