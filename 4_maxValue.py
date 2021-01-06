"Program to find maximum out of entered 3 numbers"
def max(a, b, c):
    if a > b and a > c:
        # A is Maximum
        return 1
    if b > a and b > c:
        # B is Maximum
        return 2
    if c > a and c > b:
        # C is maximum
        return 3
    
def main():
    _a = float(input("Enter A: "))
    _b = float(input("Enter B: "))
    _c = float(input("Enter C: "))
    
    _max = max(_a, _b, _c)
    if _max == 1:
        print(f"First Number [{_a}] is maximum.")
    elif _max == 2:
        print(f"Second Number [{_b}] is maximum.")
    elif _max == 3:
        print(f"Third Number [{_c}] is maximum.")
        

if __name__ == "__main__":
    main()
    
__OUTPUT__ = """
Enter A: 13
Enter B: 43
Enter C: 62
Third Number [62.0] is maximum.
"""