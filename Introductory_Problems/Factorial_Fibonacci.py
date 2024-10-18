def factorial(n=int):
    if n in (1, 0):
        result = 1
    else:
        result = n * factorial(n - 1)

    return result


print(factorial(3))


def fibonacci(n=int):
    if n in (0, 1):
        result = n
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    return result


print([fibonacci(i) for i in range(10)])
