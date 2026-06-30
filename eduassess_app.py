
import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(page_title="EduAssess AI Agent", page_icon="📝", layout="wide")

st.title("📝 EduAssess AI Agent")
st.subheader("Agentic AI Application for Quiz and Exam Generation")

st.write("""
This application helps teachers generate quizzes and exams using Generative and Agentic AI.
The agent receives assessment requirements and creates questions, answer keys, and Bloom's Taxonomy levels.
""")

with st.sidebar:
    st.header("Assessment Information")
    grade = st.text_input("Grade Level", "Grade 8")
    subject = st.text_input("Subject", "ICT")
    topic = st.text_input("Topic", "Cybersecurity")
    number_questions = st.slider("Number of Questions", 5, 30, 10)
    difficulty = st.selectbox("Difficulty Level", ["Easy", "Medium", "Hard", "Mixed"])
    question_types = st.multiselect(
        "Question Types",
        ["Multiple Choice", "True/False", "Short Answer", "Matching"],
        default=["Multiple Choice", "True/False", "Short Answer"]
    )
    generate = st.button("Generate Assessment")

def demo_assessment(grade, subject, topic, number_questions, difficulty, question_types):
    questions = []
    for i in range(1, number_questions + 1):
        if i % 3 == 1:
            questions.append(f"""
**Q{i}. Multiple Choice:** Which statement best describes {topic}?

A. It is unrelated to digital safety.  
B. It helps protect systems, data, and users.  
C. It only applies to hardware.  
D. It is used only in gaming.

**Answer:** B  
**Bloom's Level:** Understanding
""")
        elif i % 3 == 2:
            questions.append(f"""
**Q{i}. True/False:** {topic} is important for protecting personal and organizational information.

**Answer:** True  
**Bloom's Level:** Remembering
""")
        else:
            questions.append(f"""
**Q{i}. Short Answer:** Explain one real-life example of {topic}.

**Sample Answer:** A real-life example is using strong passwords and two-factor authentication to protect online accounts.  
**Bloom's Level:** Applying
""")
    return f"""
# Assessment: {topic}

## Assessment Information
- Grade: {grade}
- Subject: {subject}
- Topic: {topic}
- Number of Questions: {number_questions}
- Difficulty: {difficulty}
- Question Types: {", ".join(question_types)}

## Questions

{''.join(questions)}

## Assessment Criteria
- Accuracy of answers
- Understanding of key concepts
- Application to real-life situations
- Critical thinking

## Agentic AI Role
This AI agent supports teachers by generating structured assessments, answer keys, and learning-level classifications.
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
                {"role": "system", "content": "You are an expert assessment designer and education AI agent."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )
        return response.choices[0].message.content
    except Exception as e:
        st.warning(f"OpenAI API could not be used. Demo mode activated. Error: {e}")
        return None

if generate:
    prompt = f"""
Create a professional educational assessment.

Grade: {grade}
Subject: {subject}
Topic: {topic}
Number of Questions: {number_questions}
Difficulty: {difficulty}
Question Types: {question_types}

Include:
1. Assessment title
2. Instructions for students
3. Questions
4. Answer key
5. Bloom's Taxonomy level for each question
6. Marking criteria
7. Explanation of how this represents Agentic AI
"""
    result = generate_with_openai(prompt)
    if result is None:
        result = demo_assessment(grade, subject, topic, number_questions, difficulty, question_types)

    st.markdown(result)
    st.download_button("Download Assessment as TXT", result, "assessment.txt", "text/plain")
else:
    st.info("Enter assessment information from the sidebar and click 'Generate Assessment'.")
