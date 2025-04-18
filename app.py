import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# App title
st.title("Growth Mindset Tracker")

# Introduction
st.header("What is a Growth Mindset?")
st.write("""
A growth mindset is the belief that your abilities and intelligence can be developed through hard work, 
perseverance, and learning from your mistakes. This concept was popularized by psychologist Carol Dweck.
""")

# Key principles section
st.header("Key Principles of Growth Mindset")
principles = [
    "Embrace Challenges",
    "Learn from Mistakes",
    "Persist Through Difficulties",
    "Celebrate Effort",
    "Keep an Open Mind"
]

st.write("Here are the core principles to practice:")
for i, principle in enumerate(principles, 1):
    st.write(f"{i}. {principle}")

# Interactive challenge tracker
st.header("Your Growth Mindset Challenge Tracker")

with st.form("challenge_form"):
    challenge = st.text_input("What challenge did you face today?")
    lesson = st.text_area("What did you learn from it?")
    difficulty = st.slider("How difficult was it? (1-10)", 1, 10)
    submitted = st.form_submit_button("Submit Challenge")
    
    if submitted:
        st.success("Challenge recorded! You're growing!")
        # Here you would typically save to a database
        # For now, we'll just display it
        st.write(f"**Challenge:** {challenge}")
        st.write(f"**Lesson Learned:** {lesson}")
        st.write(f"**Difficulty Level:** {difficulty}/10")

# Visualization section
st.header("Your Growth Progress")
# Sample data - in a real app you'd track this over time
data = pd.DataFrame({
    'Week': [1, 2, 3, 4],
    'Challenges Faced': [2, 3, 5, 4],
    'Difficulty Average': [4, 5, 7, 6]
})

st.line_chart(data.set_index('Week'))

# Additional resources
st.header("Resources to Develop Your Growth Mindset")
resources = {
    "Book": "Mindset: The New Psychology of Success by Carol Dweck",
    "Video": "The Power of Believing That You Can Improve (TED Talk)",
    "Article": "How to Cultivate a Growth Mindset (Harvard Business Review)"
}

for resource_type, resource in resources.items():
    st.write(f"**{resource_type}:** {resource}")

# Footer
st.write("---")
st.write("Remember: Every challenge is an opportunity to grow!")