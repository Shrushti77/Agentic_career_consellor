import streamlit as st
import pandas as pd

# ---------- Load Data ----------
users = pd.read_csv("user_profiles.csv")
courses = pd.read_csv("course_data.csv")

# ---------- Simulated AI Response ----------
def ai_response(user_input):
    if "frontend" in user_input.lower():
        return "To become a strong Frontend Developer, start with HTML & CSS, then learn JavaScript and a framework like React."
    elif "cyber" in user_input.lower():
        return "For Cybersecurity, begin with basics of networking & ethical hacking, then progress to SOC operations and advanced security."
    elif "data" in user_input.lower():
        return "For Data Science, start with Python & statistics, then learn visualization, ML fundamentals, and deployment skills."
    elif "backend" in user_input.lower():
        return "For Backend Development, learn APIs, server-side frameworks, and progress to microservices and system design."
    else:
        return "I can help create a personalized learning roadmap. What domain are you interested in?"

# ---------- Roadmap Generator ----------
def get_roadmap(domain):
    levels_order = ["Beginner", "Intermediate", "Advanced"]
    df = courses[courses['Domain'].str.lower() == domain.lower()].copy()
    df['Level'] = pd.Categorical(df['Level'], categories=levels_order, ordered=True)
    return df.sort_values('Level')

# ---------- Streamlit UI ----------
st.set_page_config(page_title="SkillNav – AI Career Counselor", page_icon="🎓", layout="centered")

st.title("🎓 SkillNav – AI Career Counseling Companion")
st.write("An Agentic AI that helps students explore career paths and build personalized learning roadmaps. (Simulated)")

# Conversation state
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ask me about your career path (e.g., 'I want to learn frontend development')")

if st.button("Send") and user_input:
    response = ai_response(user_input)
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("SkillNav Agent", response))

# Display conversation
for sender, message in st.session_state.messages:
    st.write(f"**{sender}:** {message}")

# Show a sample roadmap
if st.button("Show Sample Roadmap for Frontend Development"):
    roadmap = get_roadmap("Frontend Development")
    st.write("### Recommended Roadmap for Frontend Development:")
    st.dataframe(roadmap)
