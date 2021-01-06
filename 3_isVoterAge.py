"Program to enter age and print the eligibility to vote or not"
def is_eligible(age:int):
    if age in range(18):
        return False
    else: 
        return True
    
def main():
    age = int(input("Enter Age in Integers: "))
    if is_eligible(age):
        print(f"You are {age} years old. You are eligible to vote.")
    else:
        print(f"You are {age} years old. You are not eligible to vote.")
        

if __name__ == "__main__":
    main()
    

__OUTPUT__ = """
Enter Age (In integers)32
You are 32 years old. You are eligible to vote. 
"""