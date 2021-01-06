"Write a Program to enterthe numbers  and to print greatestnumber using loop"

__maximum__ = 0
def main():
    global __maximum__
    __input = [int(input(f"Enter {a}th Number: ")) for a in range(1, 11)]
    for number in __input:
        if number > __maximum__:
            __maximum__ = number
    print(f"Maximum Number is {__maximum__}")

if __name__ == "__main__":
    main()

__OUTPUT__ = """
Enter 1th Number: 13
Enter 2th Number: 24
Enter 3th Number: 15
Enter 4th Number: 83
Enter 5th Number: 21
Enter 6th Number: 62
Enter 7th Number: 72
Enter 8th Number: 72
Enter 9th Number: 73
Enter 10th Number: 16
Maximum Number is 83
"""