"Write a Program to enter a number and to print its table"

def main():
    __input = int(input("Enter a Number: "))
    for i in range(0, 21):
        print(f"{__input} x {i} = {__input * i}")
    
    
if __name__ == "__main__":
    main()

__OUTPUT__ = """
Enter a Number: 13
13 x 0 = 0
13 x 1 = 13
13 x 2 = 26
13 x 3 = 39
13 x 4 = 52
13 x 5 = 65
13 x 6 = 78
13 x 7 = 91
13 x 8 = 104
13 x 9 = 117
13 x 10 = 130
13 x 11 = 143
13 x 12 = 156
13 x 13 = 169
13 x 14 = 182
13 x 15 = 195
13 x 16 = 208
13 x 17 = 221
13 x 18 = 234
13 x 19 = 247
13 x 20 = 260
"""