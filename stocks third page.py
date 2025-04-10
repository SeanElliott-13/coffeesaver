import streamlit as st

def main():
    # Page configuration
    st.set_page_config(
        page_title="Espresso Earnings",
        page_icon=":coffee:",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    # Sidebar - user inputs for steps (so it persists across pages)
    st.sidebar.header("Today's Steps")
    steps = st.sidebar.number_input(
        "Enter your total steps for today:",
        min_value=0,
        value=8743,  # default example value
        step=100,
        help="Enter the number of steps you have walked today."
    )

    # Sidebar Navigation
    st.sidebar.header("Navigation")
    page = st.sidebar.selectbox(
        "Go to",
        ["Home", "Rewards", "Leaderboard", "About"]
    )

    # -------------------------------------------
    # HOME Page
    # -------------------------------------------
    if page == "Home":
        st.title("Espresso Earnings")
        st.subheader("Walk more, save more!")
        
        daily_goal = 10000
        st.write(f"**{steps:,} / {daily_goal:,} steps**")
        
        progress_fraction = steps / daily_goal if daily_goal else 0
        st.progress(min(progress_fraction, 1.0))
        
        steps_remaining = max(daily_goal - steps, 0)
        st.write(f"**{steps_remaining:,} more steps** to reach your daily goal!")
    
    # -------------------------------------------
    # REWARDS Page
    # -------------------------------------------
    elif page == "Rewards":
        st.title("Your Coffee Rewards")

        # If user hasn't entered any steps yet, prompt them
        if steps == 0:
            st.info("Please enter your steps in the sidebar to see your rewards.")
        else:
            st.subheader(f"Today's Steps: {steps:,}")
            
            # Define coffee shop rewards
            rewards = [
                {"name": "Helix",          "discount": "15% off",           "steps_needed": 8000},
                {"name": "The Tram Cafe", "discount": "Free upsize",       "steps_needed": 10000},
                {"name": "Starbucks",     "discount": "Buy 1 Get 1 free",  "steps_needed": 15000},
            ]

            for reward in rewards:
                st.markdown(f"### {reward['name']}")
                st.write(f"**Reward:** {reward['discount']}  •  **Steps Required:** {reward['steps_needed']:,}")
                
                # Calculate user's progress for this reward
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
    
    # -------------------------------------------
    # LEADERBOARD Page
    # -------------------------------------------
    elif page == "Leaderboard":
        st.title("Step Challenge Leaderboard")
        st.subheader("Today's Top Walkers")

        # Example static leaderboard data
        # Adjust or replace with dynamic data if available
        leaderboard_data = [
            {"username": "RachelDeehan4",  "steps": 12467},
            {"username": "SeanElliott",    "steps": steps},   # Use the sidebar input for the user's steps
            {"username": "Hannah Moreau",  "steps": 7856},
        ]
        
        # Sort descending by steps
        leaderboard_data.sort(key=lambda x: x["steps"], reverse=True)
        
        # Display top 3
        if len(leaderboard_data) >= 3:
            # 1st place
            first = leaderboard_data[0]
            st.markdown(f"**1st**: {first['username']} — {first['steps']:,} steps")
            
            # 2nd place
            second = leaderboard_data[1]
            st.markdown(f"**2nd**: {second['username']} — {second['steps']:,} steps")
            
            # 3rd place
            third = leaderboard_data[2]
            st.markdown(f"**3rd**: {third['username']} — {third['steps']:,} steps")
        else:
            st.write("Not enough data for a Top 3.")
        
        # Find the user's rank and show how far they are from first
        user_entry = next((item for item in leaderboard_data if item["username"] == "SeanElliott"), None)
        
        if user_entry:
            user_index = leaderboard_data.index(user_entry)  # 0-based index
            user_rank = user_index + 1  # human-friendly rank

            st.write("---")
            st.markdown(f"**Your Rank**: {user_rank}")
            
            # Compare user steps to first place
            if user_rank == 1:
                st.write("You are currently in the lead! 🎉")
            else:
                # Steps difference from the first place
                top_steps = leaderboard_data[0]["steps"]
                diff = top_steps - user_entry["steps"]
                st.write(f"You're {diff:,} steps away from taking the lead!")
    
    # -------------------------------------------
    # ABOUT Page
    # -------------------------------------------
    elif page == "About":
        st.title("About Espresso Earnings")
        st.markdown("""
            **Espresso Earnings** is a consumer app designed to motivate you to walk more 
            by offering coffee discounts. The more steps you take, the more rewards you unlock!
            
            **Features**  
            - **Home**: Check how many steps you've taken toward your daily goal.  
            - **Rewards**: See which coffee discounts you've unlocked based on your steps.  
            - **Leaderboard**: Compare your steps to other top walkers.  
            - **About**: Learn more about the app.  
            
            **Developed by:** Your Name  
            **GitHub Repository:** [Your Repo Link](https://github.com/your-user/your-repo)
        """)

if __name__ == '__main__':
    main()
