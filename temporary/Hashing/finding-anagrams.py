
def areAnagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    s1dict = dict()
    s2dict = dict()

    for i in range(len(s1)):
        if s1[i] in s1dict:
            s1dict[s1[i]] += 1
        else:
            s1dict[s1[i]] = 1

        if s2[i] in s2dict:
            s2dict[s2[i]] += 1
        else:
            s2dict[s2[i]] = 1

    return s1dict == s2dict


if __name__ == '__main__':
    s1 = input("Enter first string : ")
    s2 = input("Enter second string : ")

    result = areAnagrams(s1, s2)
    print("Are these Strings Anagrams : ", result)
