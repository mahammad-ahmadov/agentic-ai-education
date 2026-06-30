
import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(page_title="EduPlan AI Agent", page_icon="📘", layout="wide")

st.title("📘 EduPlan AI Agent")
st.subheader("Agentic AI Application for Automatic Lesson Planning")

st.write("""
This application helps teachers generate structured lesson plans using Generative and Agentic AI.
The agent receives a teaching goal, analyzes the requirements, and produces a professional lesson plan.
""")

with st.sidebar:
    st.header("Lesson Information")
    grade = st.text_input("Grade Level", "Grade 5")
    subject = st.text_input("Subject", "ICT")
    topic = st.text_input("Topic", "Internet Safety")
    duration = st.selectbox("Lesson Duration", ["30 minutes", "45 minutes", "60 minutes", "90 minutes"])
    learning_level = st.selectbox("Student Level", ["Beginner", "Intermediate", "Advanced"])
    teaching_style = st.selectbox("Teaching Style", ["Interactive", "Project-Based", "Lecture-Based", "Group Work", "Mixed"])
    generate = st.button("Generate Lesson Plan")

def demo_lesson_plan(grade, subject, topic, duration, learning_level, teaching_style):
    return f"""
# Lesson Plan: {topic}

## 1. Lesson Information
- Grade: {grade}
- Subject: {subject}
- Topic: {topic}
- Duration: {duration}
- Student Level: {learning_level}
- Teaching Style: {teaching_style}

## 2. Learning Objectives
By the end of the lesson, students will be able to:
1. Explain the basic concept of {topic}.
2. Identify key examples related to {topic}.
3. Apply the concept in a classroom activity.
4. Reflect on the importance of {topic} in real life.

## 3. Required Materials
- Computer or projector
- Whiteboard
- Student worksheets
- Internet access if available
- Short presentation slides

## 4. Lesson Procedure

### A. Warm-Up Activity - 5 minutes
The teacher asks students what they already know about {topic}.

### B. Introduction - 10 minutes
The teacher explains the main concept using examples and visual support.

### C. Main Activity - 20 minutes
Students work individually or in groups to complete a short task related to {topic}.

### D. Discussion and Reflection - 5 minutes
Students present their answers and discuss what they learned.

### E. Assessment - 5 minutes
The teacher asks short questions to check student understanding.

## 5. Differentiation
- Beginner students receive guided examples.
- Intermediate students complete standard tasks.
- Advanced students solve extension questions.

## 6. Homework
Students write a short paragraph explaining why {topic} is important in real life.

## 7. Assessment Criteria
- Understanding of the topic
- Participation
- Accuracy of answers
- Ability to apply knowledge

## 8. Agentic AI Role
This AI agent supports teachers by planning, organizing, and generating lesson components based on user-defined goals.
"""

def generate_with_openai(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert instructional designer and education AI agent."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )
        return response.choices[0].message.content
    except Exception as e:
        st.warning(f"OpenAI API could not be used. Demo mode activated. Error: {e}")
        return None

if generate:
    prompt = f"""
Create a professional lesson plan.

Grade: {grade}
Subject: {subject}
Topic: {topic}
Duration: {duration}
Student Level: {learning_level}
Teaching Style: {teaching_style}

Include:
1. Lesson information
2. Learning objectives
3. Required materials
4. Step-by-step lesson procedure
5. Classroom activities
6. Differentiation
7. Assessment
8. Homework
9. Teacher reflection
10. Explanation of how this represents Agentic AI
"""
    result = generate_with_openai(prompt)
    if result is None:
        result = demo_lesson_plan(grade, subject, topic, duration, learning_level, teaching_style)

    st.markdown(result)
    st.download_button("Download Lesson Plan as TXT", result, "lesson_plan.txt", "text/plain")
else:
    st.info("Enter lesson information from the sidebar and click 'Generate Lesson Plan'.")
