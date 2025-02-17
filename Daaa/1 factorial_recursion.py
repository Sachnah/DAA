# Factorial of a number using recursion
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    print(f"Factorial of 6 is {fact(6)}.")
