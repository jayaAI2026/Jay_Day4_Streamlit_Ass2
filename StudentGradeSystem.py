
import streamlit as st
import base64


# -------------------------------
# Background Image
# -------------------------------

with open("BG1.avif", "rb") as file:
    image = base64.b64encode(file.read()).decode()

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/avif;base64,{image}");
        background-size: cover;
        background-position: center;
    }}

    /* Title */
    .title {{
        text-align: center;
        color: yellow;
        padding: 15px;
        border-radius: 10px;
        font-family: "Courier New", monospace;
        font-size: 40px;
        font-weight: italics;
    }}

    /* Labels */
    label {{
        color: yellow !important;
        font-weight: bold !important;
        font-family: Arial, sans-serif !important;
    }}

    /* Placeholder */
    input::placeholder {{
        color: white !important;
        opacity: 1 !important;
    }}

    /* Button */
    .stButton button {{
        background-color: lightblue !important;
        color: #4169A1 !important;
        border: 2px solid #9CC7E5 !important;
        font-weight: bold !important;
    }}

    .stButton button:hover {{
        background-color: greenyellow !important;
        color: #4169A1 !important;
    }}

    /* Result */
    .result {{
        background-color: GreenYellow;
        color: darkblue;
        padding: 20px;
        margin-top: 20px;
        border: 3px solid #9CC7E5;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# -------------------------------
# Title
# -------------------------------

st.markdown(
    '<div class="title">★ STUDENT GRADE SYSTEM ★</div>',
    unsafe_allow_html=True
)


# -------------------------------
# Student Name
# -------------------------------

student_name = st.text_input(
    "Student Name",
    placeholder="Enter student name")


# -------------------------------
# Student Marks
# -------------------------------

marks = st.number_input(
    "Student Marks",
    value=0.0,
    step=1.0
)


# -------------------------------
# Calculate Grade
# -------------------------------

if st.button("CALCULATE GRADE"):

    if student_name.strip() == "":
        st.error("Please enter the student name.")

    elif marks < 0 or marks > 100:
        st.error("Invalid marks. Marks must be between 0 and 100.")

    else:

        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "E"


        # Result
        st.markdown(
            f"""
            <div class="result">
                ★ GRADE RESULT ★<br><br>
                Student Name: {student_name}<br>
                Marks: {marks}<br>
                Grade: {grade}
            </div>
            """,
            unsafe_allow_html=True
        )