"Write a Program to find factorial of the entered number"
def factorial(number: int):
    if number == 1:
        return 1
    elif number == 0:
        return 1
    elif number < 0:
        return 'NaN'
    else:
        return number * factorial(number - 1)

def main():
    __input = int(input("Enter Integer to Calculate Factorial: "))
    print(f"Factorial of {__input} is {factorial(__input)}")
    
if __name__ == "__main__":
    main() 
    
__OUTPUT__ = """
Enter Integer to Calculate Factorial: 4
Factorial of 4 is 24
"""
