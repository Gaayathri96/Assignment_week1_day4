import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Grade Manager")
st.write("Add students, calculate grades, and view class statistics.")

# Initialize session state
if "students" not in st.session_state:
    st.session_state.students = {}


def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    elif mark >= 50:
        return "E"
    else:
        return "F"


# Add student
st.subheader("Add Student")

with st.form("student_form"):
    name = st.text_input("Student name")

    mark = st.number_input(
        "Enter marks (0–100)",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

    submitted = st.form_submit_button("Add Student")

if submitted:
    name = name.strip()

    if not name:
        st.error("Student name cannot be empty.")

    elif any(
        existing.casefold() == name.casefold()
        for existing in st.session_state.students
    ):
        st.warning("A student with this name already exists.")

    else:
        st.session_state.students[name] = {
            "mark": mark,
            "grade": calculate_grade(mark)
        }

        st.success(f"Student '{name}' added successfully!")


# Display student results
st.subheader("Student Results")

if st.session_state.students:
    rows = [
        {
            "Name": student_name,
            "Mark": details["mark"],
            "Grade": details["grade"]
        }
        for student_name, details
        in st.session_state.students.items()
    ]

    df = pd.DataFrame(rows)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # Class statistics
    marks = [
        details["mark"]
        for details in st.session_state.students.values()
    ]

    st.subheader("Class Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Class Average",
        f"{sum(marks) / len(marks):.2f}"
    )

    col2.metric("Highest Mark", max(marks))
    col3.metric("Lowest Mark", min(marks))

    # Clear all students
    if st.button("Clear All Students"):
        st.session_state.students = {}
        st.rerun()

else:
    st.info("No students added yet. Enter a name and mark above.")