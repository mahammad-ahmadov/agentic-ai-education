
# Agentic AI Capstone Applications

This package contains two simple Agentic/Generative AI applications for a Master's Capstone Project.

## Applications

1. EduPlan AI Agent
- Generates lesson plans
- Creates learning objectives
- Suggests classroom activities
- Prepares homework and assessment ideas

2. EduAssess AI Agent
- Generates exams/quizzes
- Creates MCQ, True/False, and short answer questions
- Generates answer keys
- Adds Bloom's Taxonomy levels

## How to Run

Step 1: Install Python 3.10 or newer.

Step 2: Open this folder in VS Code.

Step 3: Install requirements:

pip install -r requirements.txt

Step 4: Add OpenAI API Key.

Create a file named .env and add:

OPENAI_API_KEY=your_api_key_here

If you do not add an API key, the applications will still run using demo/template mode.

Step 5: Run EduPlan AI Agent:

streamlit run eduplan_app.py

Step 6: Run EduAssess AI Agent:

streamlit run eduassess_app.py

## Capstone Explanation

These applications demonstrate Agentic AI because they receive a user goal, analyze the task, generate structured educational output, and support teacher decision-making.
