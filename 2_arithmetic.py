" Program to enter two numbers and print the arithmetic operations like +,1,*,/,// and %."
# Functions to do operations
def addition(a, b): return a + b
def subtraction(a, b): return a - b
def multiplication(a, b): return a * b
def division(a, b): return a / b

# main function that does the operations
def main():
    alpha = float(input("Enter value of A: "))
    beta = float(input("Enter Value of B: "))
    print("Values Entered: A --> {}".format(alpha))
    print("                B --> {}".format(beta))
    print("Addition :      {}".format(addition(alpha, beta)))
    print("Subtraction :   {}".format(subtraction(alpha, beta)))
    print("Multiplication: {}".format(multiplication(alpha, beta)))
    if beta == 0.0 :
        print("Division by Zero Not Supported")
    else:
        print("Division :      {}".format(division(alpha, beta)))

if __name__ == "__main__":
    main()
    
__OUTPUT__ = """
Enter value of A: 13
Enter Value of B: 6
Values Entered: A --> 13.0
                B --> 6.0
Addition :      19.0
Subtraction :   7.0
Multiplication: 78.0
Division :      2.1666666666666665
"""