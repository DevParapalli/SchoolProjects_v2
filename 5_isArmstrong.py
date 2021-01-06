"Write a Program to check if the enterednumber is Armstrong or not."
def is_armstrong(number:int):
    __num_str = str(number)
    __sum = 0
    for digit in __num_str:
        __sum += int(digit) * int(digit) * int(digit)
    if __sum == number:
        return True
    else: 
        return False

def main():
    __check = int(input("Enter Number to Check: "))
    if is_armstrong(__check):
        print(f"Number {__check} is an Armstrong Number")
    else:
        print(f"Number {__check} is not an Armstrong Number")
        

if __name__ == "__main__":
    main()
    
__OUTPUT__ = """
Enter Number to Check: 371
Number 371 is an Armstrong Number
"""