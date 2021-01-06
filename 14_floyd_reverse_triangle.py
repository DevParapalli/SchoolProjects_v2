"Write a Program to enter the number and print the Floyd’s Triangle in decreasing order."

def reverse_floyd_triangle(iterations:int):
    __print_val = int(iterations * (iterations + 1) / 2) # n(n+1)/2
    # convert to int here since always whole number and division produces float
    for i in range(iterations + 1, 1, -1):
        for j in range(i, 1, -1):
            print(__print_val, end=" ")
            __print_val -= 1 # Decrement
        print("") # end iter j

def main():
    __input = int(input("Enter Number of iter: "))
    reverse_floyd_triangle(__input)

if __name__ == "__main__":
    main()