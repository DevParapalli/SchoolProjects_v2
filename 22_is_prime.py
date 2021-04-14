"Write a Program to show whether the entered number is prime or not"
from math import sqrt

def is_prime(number):
    # Edge Cases
    if number == 1: 
        return False
    if number == 2: 
        return True
    if number % 2 == 0: 
        print("EVEN")
        return False
    # loop through odd numbers from 3 to sqrt number (since factors pivot around this) and check remainder
    for i in range(3, int(sqrt(number)), 2): 
        if number % i == 0:
            print(i, number//i)
            return False
    return True

def main():
    __input = int(input("Enter number to check: "))
    if is_prime(__input):
        print("Number {} is Prime".format(__input))
    else:
        print("Number {} is not Prime".format(__input))
        
if __name__ == "__main__":
    main()

__OUTPUT__ = """
Enter number to check: 636726593
11131 57203
Number 636726593 is not Prime
"""