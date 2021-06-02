"Write a Program to enter the 5 subjects numbers and print the grades A/B/C/D/E"

max_marks = 80


def result(mark):
    metric = mark / max_marks
    # Validation
    if metric > 1:
        raise ValueError(f'Value {mark} is greater than maximum ({max_marks})')
    if metric < 0:
        raise ValueError(f'Marks cannot be negative.')
    # Actual Grading Logic
    if metric <= .20:
        return "E2"
    if metric <= .32:
        return "E1"
    if metric <= .40:
        return "D"
    if metric <= .50:
        return "C2"
    if metric <= .60:
        return "C1"
    if metric <= .70:
        return "B2"
    if metric <= .80:
        return "B1"
    if metric <= .90:
        return "A2"
    if metric <= 1.0:
        return "A1"


def main():
    print("let maxMarks = 80;")
    try:
        marks = {
            "subject_a": int(input("Enter Marks for Physics> ")),
            "subject_b": int(input("Enter Marks for Chemistry> ")),
            "subject_c": int(input("Enter Marks for Maths/Bio> ")),
            "subject_d": int(input("Enter Marks for English> ")),
            "subject_e": int(input("Enter Marks for PE/CS> ")),
        }
    except ValueError:
        print('Hmm, Is that a non-integral value? Marks are integers, you know.')
        main()
    for key in marks:
        if marks[key] > max_marks:
            raise ValueError(f'Value {marks[key]} is greater than maximum ({max_marks})')
    # We 
    total = sum([marks[key] for key in marks])
    average = total / len(marks)
    
    # Formatted Strings to look good.
    print(f"""
Grade for Physics: {result(marks["subject_a"])},
Grade for Chemistry: {result(marks["subject_b"])},
Grade for Maths/Bio: {result(marks["subject_c"])},
Grade for English: {result(marks["subject_d"])},
Grade for PE/CS: {result(marks["subject_e"])},
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
