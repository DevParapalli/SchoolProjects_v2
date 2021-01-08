LIST = []

def populate():
    global LIST
    __input = input("Enter CSVs: ")
    LIST += __input.split(',')
    LIST = [int(n) for n in LIST]

def main():
    populate()
    print(LIST)
    LIST.sort()
    print(LIST)

if __name__ == "__main__":
    main()


__OUTPUT__ = """
Enter CSVs: 13, 16, 84, 18, 74
[13, 16, 84, 18, 74]
[13, 16, 18, 74, 84]
"""