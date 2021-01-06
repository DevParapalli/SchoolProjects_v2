LIST = []

def populate():
    global LIST
    __input = input("Enter CSVs: ")
    LIST += __input.split(',')

def main():
    populate()
    print(LIST)
    LIST.sort()
    print(LIST)

if __name__ == "__main__":
    main()
