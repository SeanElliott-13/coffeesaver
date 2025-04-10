import streamlit as st

def main():
    # Page configuration for nicer display on Streamlit Cloud
    st.set_page_config(
        page_title="Espresso Earnings",
        page_icon=":coffee:",
        layout="centered",  # or "wide"
        initial_sidebar_state="collapsed"
    )
    
    # -------------------------
    # Header / Title Section
    # -------------------------
    st.title("Espresso Earnings")
    st.subheader("Walk more, save more!")
    
    # -------------------------
    # Total Steps & Progress
    # -------------------------
    daily_goal = 10000
    total_steps = 8743  # Replace this with a dynamic value from a database or API if needed
    steps_remaining = daily_goal - total_steps
    
    # Show the steps and a progress bar
    st.write(f"**{total_steps:,} / {daily_goal:,} steps**")  # format with commas
    st.progress(total_steps / daily_goal)
    st.write(f"**{steps_remaining:,} more steps** to reach your daily goal!")
    
    # -------------------------
    # Rewards Section
    # -------------------------
    st.header("Your Rewards")

    # Define a list of rewards: name, description, steps_needed, and progress
    rewards = [
        {
            "name": "Helix",
            "description": "15% off",
            "steps_needed": 8000,
        },
        {
            "name": "The Tram Cafe",
            "description": "Free upsize",
            "steps_needed": 10000,
        },
        {
            "name": "Starbucks",
            "description": "Buy 1 Get 1",
            "steps_needed": 15000,
        }
    ]
    
    # Display each reward with progress
    for reward in rewards:
        st.subheader(f"{reward['name']}")
        st.write(f"{reward['description']} – **{reward['steps_needed']:,} steps needed**")
        
        # Calculate user's progress toward each reward
        # If user steps exceed steps_needed, they can claim the reward (or you can cap at 100%)
        progress_fraction = total_steps / reward['steps_needed']
        if progress_fraction >= 1:
            st.write(":tada: **Ready to use!**")
            st.progress(1.0)
        else:
            st.write(f"{int(progress_fraction * 100)}% progress")
            st.progress(progress_fraction)
        
        st.write("---")  # visual separator

if __name__ == "__main__":
    main()
