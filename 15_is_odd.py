#! python -i
"Write a Program to enter the number and print whether the number is odd or even"

def is_odd(n:int):
    if n % 2 != 0:
        return True
    else:
        return False

def main():
    __input = int(input("Enter Number to Check: "))
    if is_odd(__input):
        print(f"Number {__input} is ODD")
    else:
        print(f"Number {__input} is EVEN")

if __name__ == "__main__":
    main()

__OUTPUT__ = """
Enter Number to Check: 13
Number 13 is ODD
"""