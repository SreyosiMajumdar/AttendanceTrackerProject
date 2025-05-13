import csv
import datetime
import os

FILENAME = 'attendance.csv'
STUDENT_FILE = 'students.txt'

def load_students():
    if not os.path.exists(STUDENT_FILE):
        print("students.txt not found. Please create it with student names.")
        return []
    with open(STUDENT_FILE, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def initialize_csv(students):
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date"] + students)

def mark_attendance(students):
    today = datetime.date.today().isoformat()
    attendance = []

    print(f"\nMark attendance for {today}:\n(Type 'P' for Present, 'A' for Absent)")
    for student in students:
        status = input(f"{student}: ").strip().upper()
        while status not in ['P', 'A']:
            status = input(f"Invalid input. Enter P or A for {student}: ").strip().upper()
        attendance.append(status)

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([today] + attendance)

    print("\n Attendance marked successfully!\n")

def view_attendance():
    if not os.path.exists(FILENAME):
        print("\n No attendance records found.\n")
        return

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("\t".join(row))

def main():
    students = load_students()
    if not students:
        return

    initialize_csv(students)

    while True:
        print("\n===== Attendance Tracker =====")
        print("1. Mark Attendance")
        print("2. View Attendance Records")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            mark_attendance(students)
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            print(" Exiting the Attendance Tracker.")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
