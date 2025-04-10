import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    # Configure the app page
    st.set_page_config(
        page_title="Espresso Earnings",
        page_icon=":coffee:",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    # ----------------------------------------------------------------------------
    # Sidebar: User Input & Navigation
    # ----------------------------------------------------------------------------
    st.sidebar.header("Today's Steps")
    steps = st.sidebar.number_input(
        "Enter your total steps for today:",
        min_value=0,
        value=8743,  # default example value
        step=100,
        help="Enter the number of steps you have walked today."
    )

    st.sidebar.header("Navigation")
    page = st.sidebar.selectbox(
        "Go to",
        ["Home", "Rewards", "Leaderboard", "Settings", "About"]
    )

    # ----------------------------------------------------------------------------
    # HOME Page
    # ----------------------------------------------------------------------------
    if page == "Home":
        st.title("Espresso Earnings")
        st.subheader("Walk more, save more!")
        
        daily_goal = 10000
        st.write(f"**{steps:,} / {daily_goal:,} steps**")
        progress_fraction = steps / daily_goal if daily_goal else 0
        st.progress(min(progress_fraction, 1.0))
        steps_remaining = max(daily_goal - steps, 0)
        st.write(f"**{steps_remaining:,} more steps** to reach your daily goal!")

    # ----------------------------------------------------------------------------
    # REWARDS Page
    # ----------------------------------------------------------------------------
    elif page == "Rewards":
        st.title("Your Coffee Rewards")
        if steps == 0:
            st.info("Please enter your steps in the sidebar to see your rewards.")
        else:
            st.subheader(f"Today's Steps: {steps:,}")
            rewards = [
                {"name": "Helix",          "discount": "15% off",          "steps_needed": 8000},
                {"name": "The Tram Cafe",  "discount": "Free upsize",      "steps_needed": 10000},
                {"name": "Starbucks",      "discount": "Buy 1 Get 1 free", "steps_needed": 15000},
            ]
            for reward in rewards:
                st.markdown(f"### {reward['name']}")
                st.write(f"**Reward:** {reward['discount']}  •  **Steps Required:** {reward['steps_needed']:,}")
                progress = steps / reward['steps_needed']
                if progress >= 1:
                    st.write("🎉 **Reward Unlocked!**")
                    st.progress(1.0)
                else:
                    st.write(f"Progress: {int(progress * 100)}%")
                    st.progress(min(progress, 1.0))
                    remaining = reward['steps_needed'] - steps
                    st.write(f"Steps needed to unlock: {remaining:,}")
                st.write("---")

    # ----------------------------------------------------------------------------
    # LEADERBOARD Page with Bar Chart
    # ----------------------------------------------------------------------------
    elif page == "Leaderboard":
        st.title("Step Challenge Leaderboard")
        st.subheader("Today's Top Walkers")

        # Example leaderboard data; user's steps are integrated
        leaderboard_data = [
            {"username": "RachelDeehan4", "steps": 12467},
            {"username": "SeanElliott",   "steps": steps},  # Use sidebar input for user's steps
            {"username": "Hannah Moreau", "steps": 7856},
        ]
        # Sort the leaderboard data in descending order by steps
        leaderboard_data.sort(key=lambda x: x["steps"], reverse=True)
        
        # Convert the leaderboard data to a DataFrame
        df = pd.DataFrame(leaderboard_data)

        # Create a horizontal bar chart using Plotly Express
        fig = px.bar(
            df,
            x="steps",
            y="username",
            orientation="h",
            text="steps",
            labels={"username": "User", "steps": "Steps"},
            title="Leaderboard - Top Walkers"
        )
        # Ensure that the highest step count appears at the top
        fig.update_layout(yaxis={'categoryorder':'total ascending'})
        fig.update_traces(texttemplate='%{text}', textposition='outside')
        st.plotly_chart(fig, use_container_width=True)

        # Determine the user's rank and display additional info
        user_entry = next((item for item in leaderboard_data if item["username"] == "SeanElliott"), None)
        if user_entry:
            user_rank = leaderboard_data.index(user_entry) + 1  # convert from 0-based index
            st.markdown(f"**Your Rank:** {user_rank}")
            if user_rank != 1:
                diff = leaderboard_data[0]["steps"] - user_entry["steps"]
                st.markdown(f"You're {diff:,} steps away from the top!")

    # ----------------------------------------------------------------------------
    # SETTINGS Page
    # ----------------------------------------------------------------------------
    elif page == "Settings":
        st.title("Settings")
        st.subheader("Sean @SeanElliott")
        st.write("Coffee Enthusiast, Member since 2023")
        st.markdown("### Account")
        st.write("Profile (coming soon!)")
        notifications_enabled = st.checkbox("Notifications", value=True)
        daily_step_goal = st.number_input("Daily Step Goal", min_value=1000, max_value=30000, value=10000, step=1000)
        st.markdown("### App Settings")
        dark_mode = st.checkbox("Dark Mode", value=False)
        default_map_view = st.selectbox("Default Map View", ["DCU Campus", "City Center", "Suburbs"])
        st.write("Connected Devices: Fitbit Versa")
        st.markdown("---")
        st.write("**Selected Settings**")
        st.write(f"- Notifications: {'On' if notifications_enabled else 'Off'}")
        st.write(f"- Daily Step Goal: {daily_step_goal:,}")
        st.write(f"- Dark Mode: {'On' if dark_mode else 'Off'}")
        st.write(f"- Map View: {default_map_view}")

    # ----------------------------------------------------------------------------
    # ABOUT Page
    # ----------------------------------------------------------------------------
    elif page == "About":
        st.title("About Espresso Earnings")
        st.markdown("""
            **Espresso Earnings** is a consumer app that motivates you to walk more 
            by offering coffee discounts. The more steps you take, the more rewards you unlock!
            
            **Features**  
            - **Home**: Track how many steps you've taken towards a daily goal.  
            - **Rewards**: Check which coffee discounts you unlock based on your steps.  
            - **Leaderboard**: Compare your steps to other top walkers via a bar chart.  
            - **Settings**: Customize your daily step goal, notifications, and more.  
            - **About**: Learn about the app.  
            
            **Developed by:** Your Name  
            **GitHub Repository:** [Your Repo Link](https://github.com/your-username/your-repo)
        """)

if __name__ == "__main__":
    main()
