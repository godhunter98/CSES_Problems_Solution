n = int(input())


def get_substrings(n):
    result = 1
    result = result * (2**n)
    result = result % (10**9 + 7)
    return result


print(get_substrings(n))
