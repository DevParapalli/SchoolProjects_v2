"Write a Program to enter the 5 subjects numbers and print the grades A/B/C/D/E"

__max_marks__ = 80

def result(mark):
    __metric = mark / (__max_marks__)
    if __metric <= 0.4125: return "F"
    if __metric <= 0.625: return "D"
    if __metric <= 0.75: return "C"
    if __metric <= 0.875: return "B"
    if __metric <= 1.0: return "A"

def main():
    print("let maxMarks = 80;")
    marks = {
        "subject_a": int(input("Enter Marks for Subject A: ")),
        "subject_b": int(input("Enter Marks for Subject B: ")),
        "subject_c": int(input("Enter Marks for Subject C: ")),
        "subject_d": int(input("Enter Marks for Subject D: ")),
        "subject_e": int(input("Enter Marks for Subject E: ")),
    }
    total = sum([marks[key] for key in marks])
    average = total / 5
    print(f"""
Grade for A: {result(marks["subject_a"])},
Grade for B: {result(marks["subject_b"])},
Grade for C: {result(marks["subject_c"])},
Grade for D: {result(marks["subject_d"])},
Grade for E: {result(marks["subject_e"])},
Average Grade: {result(average)}
    """)

if __name__ == "__main__":
    main()



__OUTPUT__ = """
let maxMarks = 80;
Enter Marks for Subject A: 79
Enter Marks for Subject B: 73
Enter Marks for Subject C: 61
Enter Marks for Subject D: 51
Enter Marks for Subject E: 80

Grade for A: A,
Grade for B: A,
Grade for C: B,
Grade for D: C,
Grade for E: A,
Average Grade: B
"""