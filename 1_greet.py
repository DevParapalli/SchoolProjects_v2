""" Write a program to enter name and display as Hello, Name. """
def greet():
    _name = input("Enter Your Name:")
    print(f"Hello {_name}")
    return f"Hello {_name}"

if __name__ == "__main__":
    greet()

__OUTPUT__ = """
Enter Your Name:Dev
Hello Dev
"""