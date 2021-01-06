"Write a Program to show the outputs based on entered list."

LIST = [13, 14, 81, "Python", "CBSE", 4.0, [1, 2]]

def main():
    # Get element from list
    print(LIST[1]) # 14
    # Nested List
    print(LIST[6]) # [1, 2]
    print(LIST[6][1]) # 2
    # List + String Indexing
    print(LIST[4]) # CBSE
    print(LIST[4][1]) # B

if __name__ == "__main__":
    main()

__OUTPUT__ = """
14
[1, 2]
2
CBSE
B
"""