"Write a Program to enterthe string  and to check if it’s palindrome or not using loop."

def is_palindrome(str_obj):
    if len(str_obj) < 1:
        return True
        # blank string is a palindrome
    else:
        if str_obj[0] == str_obj[-1]:
            return is_palindrome(str_obj[1:-1])
        else:
            return False

def main():
    __input = input("Enter String to Check: ").strip() 
    # Removing extra whitespace to make compare easier
    print(is_palindrome(__input))
    

if __name__ == "__main__":
    main()

__OUTPUT__ = """
Enter String to Check: madam
True
"""


