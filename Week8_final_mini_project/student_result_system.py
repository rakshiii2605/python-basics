students = {}

def add_student(name, marks):
    students[name] = marks

def calculate_average(marks):
    return sum(marks) / len(marks)

def display_results():
    print("\n📊 Student Results:")
    for name, marks in students.items():
        avg = calculate_average(marks)
        print(f"{name}: Marks = {marks}, Average = {avg:.2f}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Student\n2. View Results\n3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            marks = list(map(int, input("Enter marks separated by space: ").split()))
            add_student(name, marks)
        elif choice == "2":
            display_results()
        elif choice == "3":
            print("👋 Exiting Student Result System.")
            break
        else:
            print("❌ Invalid choice. Try again.")
