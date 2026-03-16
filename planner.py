import os
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_study_plan(subjects, exam_date, hours_per_day):

    today = datetime.today().date()
    days_left = (exam_date - today).days

    # Prevent invalid exam dates
    if days_left <= 0:
        return "⚠️ The exam date must be in the future."

    prompt = f"""
You are an AI study planning assistant.

Subjects: {subjects}

The exam date is {exam_date}.
There are {days_left} days remaining.

The student can study {hours_per_day} hours per day.

Rules:
- Allocate more time to difficult subjects.
- Rotate subjects across days.
- Reserve the final day for revision.
- Avoid repeating the same subject too many times in one day.

Create a clear day-by-day schedule.
"""

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.1-8b-instant",
    )

    return chat_completion.choices[0].message.content
