"Write a Program to find factorial of entered number "
"using library functionfact()"
import math


def main():
    __num = int(input("Enter Number: "))
    print(f"{__num}! = {math.factorial(__num)}")


if __name__ == "__main__":
    main()

__OUTPUT__ = """ 
Enter Number: 6
6! = 720
"""
