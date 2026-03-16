import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from planner import generate_study_plan

st.markdown(
"""
<h1>
<span style="color:#FF7A00;">StudyAgent</span> – AI-powered exam study planner
</h1>
""",
unsafe_allow_html=True
)

st.write("Enter your study details and generate a personalized plan.")

subjects = st.text_input("Subjects (comma separated)")

exam_date = st.date_input("Enter your exam date")

hours = st.number_input("Study hours per day", min_value=1, max_value=12)

if st.button("Generate Study Plan"):

    plan = generate_study_plan(subjects, exam_date, hours)

    st.subheader("Your Study Plan")

    st.write(plan)

    st.download_button(
    label="⬇ Download Study Plan",
    data=plan,
    file_name="study_plan.txt",
    mime="text/plain"
)


    # Create better looking chart
subject_list = [s.strip() for s in subjects.split(",")]
hours_per_subject = hours / len(subject_list)

data = {
    "Subject": subject_list,
    "Study Hours": [hours_per_subject] * len(subject_list)
}

df = pd.DataFrame(data)

fig = px.bar(
    df,
    x="Subject",
    y="Study Hours",
    title="📊 Study Hours Distribution",
    color="Subject"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("✅ Track Your Study Progress")

subject_list = [s.strip() for s in subjects.split(",")]

completed = []

for subject in subject_list:
    if st.checkbox(subject):
        completed.append(subject)

progress = len(completed) / len(subject_list)

st.progress(progress)

st.write(f"Progress: {int(progress*100)}% completed")
