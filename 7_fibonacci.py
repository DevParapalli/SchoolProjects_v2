"Write a Program to enter the number of terms and to print the Fibonacci Series."
from math import sqrt

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif number < 0:
        return 'ValueError: Value too small.'
    else:
        return fibonacci(number-1) + fibonacci(number-2)
    

def alternate_fib(number):
    sqrt_5 = sqrt(5)
    phi = (1 + sqrt_5)/2
    psi = (1 - sqrt_5)/2
    return round((phi**number - psi**number)/sqrt_5)

def main():
    import time
    __no_of_terms = int(input("Number of Terms of Fibonacci: "))
    #t1 = time.time()
    #__list = [fibonacci(number) for number in range(__no_of_terms)]
    #print(f"Fibonacci Numbers up to {__no_of_terms}th term is {__list} ")
    t2 = time.time()
    __list_alt = [alternate_fib(number) for number in range(__no_of_terms)]
    print(f"Fibonacci Numbers up to {__no_of_terms}th term is {__list_alt} ")
    #print("A {}".format(time.time() - t1))
    print("B {}".format(time.time() - t2))
if __name__ == "__main__":
    main()
    
__OUTPUT__ = """
Fibonacci Numbers up to 13th term is [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
"""