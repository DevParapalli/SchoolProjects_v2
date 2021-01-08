"Write a Program to show whether the entered number is prime or not"

def is_prime(number:int) -> bool:
    # Edge Cases
    if number == 1: return False
    
    # loop through all numbers from 2 to number and check remainder
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def main():
    __input = int(input("Enter number to check: "))
    if is_prime(__input):
        print(f"Number {__input} is Prime")
    else:
        print(f"Number {__input} is not Prime")
        
if __name__ == "__main__":
    main()

__OUTPUT__ = """
Enter number to check: 13
Number 13 is Prime
"""