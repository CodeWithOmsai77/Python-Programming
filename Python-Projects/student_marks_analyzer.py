"""Summarize marks for a student using lists, loops, and functions."""


def read_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a numeric mark.")


def grade_from_average(average):
    if average >= 90:
        return "A"
    if average >= 75:
        return "B"
    if average >= 60:
        return "C"
    if average >= 40:
        return "D"
    return "F"


def main():
    name = input("Enter student name: ").strip()
    while not name:
        name = input("Name cannot be empty. Enter student name: ").strip()

    subjects = ["Python", "Mathematics", "Computer Science"]
    marks = [read_mark(subject) for subject in subjects]
    total = sum(marks)
    average = total / len(marks)

    print("\n===== Student Marks Report =====")
    print(f"Student: {name}")
    for subject, mark in zip(subjects, marks):
        print(f"{subject:<20} {mark:6.2f}")
    print("-" * 29)
    print(f"Total:   {total:.2f} / {len(subjects) * 100}")
    print(f"Average: {average:.2f}%")
    print(f"Grade:   {grade_from_average(average)}")


if __name__ == "__main__":
    main()
