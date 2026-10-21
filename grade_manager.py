import streamlit as st
# Student Grade Manager
# With Error Handling

students = {}

st.title("Student Grade Manager")
st.write("Streamlit is working!")

name = st.text_input("Student name")
mark = st.number_input("Enter marks", 0, 100, 0)

if st.button("Calculate Grade"):
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    elif mark >= 50:
        grade = "E"
    else:
        grade = "F"

    st.success(f"{name}: Grade {grade}")


def add_student():
    """Add a student with error handling."""

    try:
        name = input("Enter student name: ").strip()

        # Check for empty name
        if not name:
            raise ValueError("Student name cannot be empty.")

        # Check for duplicate name
        if name in students:
            print("Warning: A student with this name already exists.")
            return

        # Get mark
        mark_input = input("Enter mark (0-100): ").strip()

        # Convert mark to a number
        mark = float(mark_input)

        # Validate mark range
        if mark < 0 or mark > 100:
            raise ValueError("Mark must be between 0 and 100.")

        # Calculate grade
        grade = calculate_grade(mark)

        # Store student information
        students[name] = {
            "mark": mark,
            "grade": grade
        }

        print(f"Student '{name}' added successfully!")

    except ValueError as error:
        print(f"Error: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")


def display_students():
    """Display all students in a formatted table."""

    try:
        if not students:
            print("No students available.")
            return

        print("\n" + "=" * 45)
        print(f"{'Name':<20}{'Mark':<10}{'Grade':<10}")
        print("-" * 45)

        for name, details in students.items():
            print(
                f"{name:<20}"
                f"{details['mark']:<10.2f}"
                f"{details['grade']:<10}"
            )

        print("=" * 45)

    except Exception as error:
        print(f"Error displaying students: {error}")


def show_statistics():
    """Display class statistics."""

    try:
        if not students:
            print("No student data available.")
            return

        marks = [details["mark"] for details in students.values()]

        average = sum(marks) / len(marks)
        highest = max(marks)
        lowest = min(marks)

        print("\n===== CLASS STATISTICS =====")
        print(f"Class Average : {average:.2f}")
        print(f"Highest Mark  : {highest:.2f}")
        print(f"Lowest Mark   : {lowest:.2f}")

    except ZeroDivisionError:
        print("Error: Cannot calculate the average because there are no marks.")

    except Exception as error:
        print(f"Error calculating statistics: {error}")


def main():
    """Main menu of the Student Grade Manager."""

    while True:
        try:
            print("\n===== STUDENT GRADE MANAGER =====")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Show Class Statistics")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == "1":
                add_student()

            elif choice == "2":
                display_students()

            elif choice == "3":
                show_statistics()

            elif choice == "4":
                print("Thank you for using Student Grade Manager!")
                break

            else:
                print("Error: Invalid choice. Please enter a number from 1 to 4.")

        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            break

        except Exception as error:
            print(f"Unexpected error: {error}")


# Run the program
if __name__ == "__main__":
    main()