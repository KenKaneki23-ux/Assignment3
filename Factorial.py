def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n=int(input('Enter number for Factorial: '))
print(f"The Factorial of {n} is {factorial(n)}")