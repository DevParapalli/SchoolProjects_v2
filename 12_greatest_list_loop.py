"Write a Program to enter thenumbers  in a list and to show the greatest elementusing loop in the entered list."

LIST = [13, 14, 81, 41, 25, 75, 12, 74, 64]


def main():
    __maximum__ = 0
    for number in LIST:
        if number > __maximum__:
            __maximum__ = number
    print(f"Maximum Number is {__maximum__}")

if __name__ == "__main__":
    main()