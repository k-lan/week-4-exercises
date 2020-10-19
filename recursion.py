# Chapter 5 recursion exercises

# Factorial 7 is 1x2x3x4x5x6x7
def factorial(fact_int):
    """
    Calculate the factorial of entered number
    :param fact_int: number to get the factorial of
    :return: int: factorial
    """
    if fact_int <= 1:  # We are at the first multiplication number or below, base case
        return 1
    else:
        return fact_int * factorial(fact_int - 1)  # Changes state and moves towards base case


def reverse(s):
    """
    Reverse string s
    :param s: string
    :return: reversed string
    """
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


# Fibonacci is 0 1 1 2 3 5 8 13 21
def fibonacci_slow(num: int):  # Returns fibonacci number using recursion
    if num <= 0:
        "Please enter a value above 0"
    elif num == 1:  # First fib number is 0
        return 0
    elif num == 2:  # second fib number is 1
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def fibonacci(num: int):
    first = 0
    second = 1
    if num <= 0:
        print("Incorrect input")
    elif num == 1:
        return second
    else:
        for x in range(2, num):
            sum = first + second
            first = second
            second = sum
        return second


"""_______________Book Examples___________________"""


def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])


def to_str(n, base):
    symbols = '0123456789ABCDEF'
    if n < base:
        return symbols[n]
    else:
        return to_str(n // base, base) + symbols[n % base]


"""_________________________________________________"""


def main():
    print(listsum([1, 3, 5, 7, 9]))
    print(to_str(9, 10))
    print(factorial(7))
    print(reverse("hello"))
    print(fibonacci(0))
    print(fibonacci_slow(0))


if __name__ == '__main__':
    main()