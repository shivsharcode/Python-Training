def example(L):

    i =1
    result = []
    while i < len(L):
        result.append(L[i])
        print(result)
        i = i + 3

    return result

print(example([1,2,3,4,5]))