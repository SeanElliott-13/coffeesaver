import random
import streamlit as st
import matplotlib.pyplot as plt

# =============================================================================
# Initialize session state variables if not already present
# =============================================================================
if "users" not in st.session_state:
    # Conversion: 1 point per 1000 steps
    users = {
        "Emma": {"steps": 0, "points": 0},
        "Sean": {"steps": 0, "points": 0},
        "Rachel": {"steps": 0, "points": 0},
        "You": {"steps": 0, "points": 0}
    }
    # Give mock initial steps/points for users except "You"
    for name in users:
        if name != "You":
            initial_steps = random.randint(5000, 20000)
            users[name]["steps"] = initial_steps
            users[name]["points"] = initial_steps // 1000  # 1 point per 1000 steps
            users[name]["daily_steps"] = []  # initialize empty daily record
    # "You" starts with zero steps and an empty daily record
    users["You"]["daily_steps"] = []
    st.session_state.users = users

if "cafes" not in st.session_state:
    cafes = [
        {"name": "The Helix Cafe", "points_required": 50, "rating": 4.5},
        {"name": "The Tram Cafe", "points_required": 30, "rating": 4.2},
        {"name": "Starbucks", "points_required": 75, "rating": 4.8}
    ]
    st.session_state.cafes = cafes

# =============================================================================
# App Title and Description
# =============================================================================
st.title("Fitness-Coffee Reward App Simulation")
st.write("Simulate a
