"Write a Program to enter the 5 subjects numbers and print the grades A/B/C/D/E"

__max_marks__ = 80

def result(mark):
    __metric = mark / (__max_marks__/2)
    if __metric <= 0.825: return "F"
    if __metric <= 1.25: return "D"
    if __metric <= 1.5: return "C"
    if __metric <= 1.75: return "B"
    if __metric <= 2.0: return "A"

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
Enter Marks for Subject A: 20
Enter Marks for Subject B: 60
Enter Marks for Subject C: 80
Enter Marks for Subject D: 80
Enter Marks for Subject E: 80

Grade for A: F,
Grade for B: C,
Grade for C: A,
Grade for D: A,
Grade for E: A,
Average Grade: B
"""