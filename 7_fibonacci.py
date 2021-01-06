"Write a Program to enter the number of terms and to print the Fibonacci Series."
def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif number < 0:
        return 'ValueError: Value too small.'
    else:
        return fibonacci(number-1) + fibonacci(number-2)
    

def main():
    __no_of_terms = int(input("Number of Terms of Fibonacci: "))
    __list = [fibonacci(number) for number in range(__no_of_terms)]
    print(f"Fibonacci Numbers up to {__no_of_terms}th term is {__list} ")

if __name__ == "__main__":
    main()
    
__OUTPUT__ = """
Fibonacci Numbers up to 13th term is [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
"""