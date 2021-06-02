"Write a Program to enter the number of terms and to print the Fibonacci Series."
from math import sqrt


def fibonacci(number:int):
    sqrt_5 = sqrt(5)
    phi = (1 + sqrt_5)/2
    psi = (1 - sqrt_5)/2
    return round((phi**number - psi**number)/sqrt_5)


def main():
    import time
    no_of_terms = int(input("Number of Terms of Fibonacci: "))
    t1 = time.time()
    list_of_fib_num = [fibonacci(number) for number in range(no_of_terms)]
    print(
        f"Fibonacci Numbers up to {no_of_terms}th term is {list_of_fib_num} ")
    print("Time Taken: {}".format(time.time() - t1))


if __name__ == "__main__":
    main()

__OUTPUT__ = """
Fibonacci Numbers up to 13th term is [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
"""
