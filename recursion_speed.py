import recursion
from timeit import Timer

def time_1():
    return recursion.fibonacci(2000)

def time_2():
    return recursion.fibonacci_slow(2000)

def main():
    t1 = Timer("time_1()", "from __main__ import time_1")
    print("Typical speed speed:  ", t1.timeit(number=1000), "milliseconds")
    t2 = Timer("time_2()", "from __main__ import time_2")
    print("Recursion speed:      ", t2.timeit(number=1000), "milliseconds")
    print("Both seem to be O(n), the faster one has been inconsistent, "
          "I sometimes see the recursive function compute faster and"
          "others I see the normal function compute quicker")


if __name__ == '__main__':
    main()