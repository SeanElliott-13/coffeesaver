import streamlit as st

def main():
    # Set the app's page configuration for a polished display on Streamlit Cloud.
    st.set_page_config(
        page_title="Coffee Rewards",
        page_icon=":coffee:",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    # ----------------------------------------------------------------------------
    # SIDEBAR
    # ----------------------------------------------------------------------------
    st.sidebar.header("User Info")
    # Persistent input for total steps (available on every page)
    steps = st.sidebar.number_input(
        "Enter your total steps for today:",
        min_value=0,
        value=0,
        step=100,
        help="Enter the number of steps you have walked today."
    )
    
    st.sidebar.header("Navigation")
    # Navigation menu for switching between pages
    page = st.sidebar.selectbox("Select Page", ["Home", "Rewards", "About"])

    # ----------------------------------------------------------------------------
    # PAGE: Home
    # ----------------------------------------------------------------------------
    if page == "Home":
        st.title("Coffee Rewards")
        st.markdown("Welcome to **Coffee Rewards**! Walk more today and unlock exclusive coffee discounts.")
        if steps > 0:
            st.subheader(f"Total Steps Walked Today: {steps:,}")
            # Optionally, show a simple progress indicator towards a baseline daily goal (e.g., 10,000 steps)
            daily_goal = 10000
            progress = min(steps / daily_goal, 1.0)
            st.progress(progress)
            st.write(f"Progress toward a {daily_goal:,} steps goal: {int(progress*100)}%")
        else:
            st.info("Please enter your steps in the sidebar.")

    # ----------------------------------------------------------------------------
    # PAGE: Rewards
    # ----------------------------------------------------------------------------
    elif page == "Rewards":
        st.title("Your Coffee Rewards")
        if steps > 0:
            st.subheader(f"Steps Walked: {steps:,}")
            # Define coffee shop rewards with the associated discount and required steps
            rewards = [
                {"name": "Helix", "discount": "15% off", "steps_needed": 8000},
                {"name": "The Tram Cafe", "discount": "Free upsize", "steps_needed": 10000},
                {"name": "Starbucks", "discount": "Buy 1 Get 1 free", "steps_needed": 15000}
            ]
            
            # Display each reward with progress information
            for reward in rewards:
                st.markdown(f"### {reward['name']}")
                st.write(f"**Reward:** {reward['discount']}  •  **Steps Required:** {reward['steps_needed']:,}")
                progress = steps / reward['steps_needed']
                
                if progress >= 1:
                    st.write("🎉 **Reward Unlocked!**")
                    st.progress(1.0)
                else:
                    st.write(f"Progress: {int(progress * 100)}%")
                    st.progress(progress if progress <= 1.0 else 1.0)
                    remaining = reward['steps_needed'] - steps
                    st.write(f"Steps needed to unlock: {remaining:,}")
                st.write("---")
        else:
            st.info("Please enter your steps in the sidebar to see your rewards.")

    # ----------------------------------------------------------------------------
    # PAGE: About
    # ----------------------------------------------------------------------------
    elif page == "About":
        st.title("About Coffee Rewards")
        st.markdown("""
            **Coffee Rewards** is a consumer application designed to help you earn coffee discounts by walking more!
            
            **How It Works:**
            - Enter your total steps for today in the sidebar.
            - The app calculates your progress towards unlocking exclusive coffee discounts.
            - When you reach the required number of steps for a reward, that discount becomes available.
            
            Stay active, enjoy your coffee, and get rewarded!
        """)

if __name__ == '__main__':
    main()


