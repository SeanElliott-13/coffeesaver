
 
# Fitness-Coffee Reward App Simulation in Colab
# (Python script implementing core features with ipywidgets)

import random
from IPython.display import display, clear_output
import ipywidgets as widgets
import matplotlib.pyplot as plt

# 1. Initialize users and conversion (daily steps -> points) [Features 1 & 2]
# Assume 1 point per 1000 steps for simplicity (e.g., 10,000 steps = 10 points).
points_per_step = 1/1000  # conversion ratio
users = {
    "Emma": {"steps": 0, "points": 0},
    "Sean": {"steps": 0, "points": 0},
    "Rachel": {"steps": 0, "points": 0},
    "You": {"steps": 0, "points": 0}
}
# Give mock initial steps/points for the leaderboard (except "You" starts at 0)
for name in users:
    if name != "You":
        initial_steps = random.randint(5000, 20000)  # random past steps for demo
        users[name]["steps"] = initial_steps
        users[name]["points"] = initial_steps // 1000  # integer points (1 per 1000 steps)

# 2. Prepare partner cafes mock data [Feature 3]
cafes = [
    {"name": "The Helix Cafe", "points_required": 50, "rating": 4.5},
    {"name": "The Tram Cafe", "points_required": 30, "rating": 4.2},
    {"name": "Starbucks", "points_required": 75, "rating": 4.8}
]

# 3. Set up interactive widgets (dropdown for user selection, button to simulate steps) [Feature 4]
user_dropdown = widgets.Dropdown(
    options=list(users.keys()),
    value="You",  # default selected user
    description="User:"
)
simulate_btn = widgets.Button(description="Simulate Day")

# Use an Output widget to capture prints/plots from the callback&#8203;:contentReference[oaicite:4]{index=4}
output_area = widgets.Output()

# Show initial leaderboard and cafe list in the output area
with output_area:
    clear_output()
    # Leaderboard sorted by points (highest first)
    leaderboard = sorted(users.items(), key=lambda x: x[1]['points'], reverse=True)
    print("🏅 Initial Leaderboard:")
    for rank, (uname, data) in enumerate(leaderboard, start=1):
        print(f"  {rank}. {uname} — {data['points']} points")
    print("\n☕ Nearby Partner Cafes:")
    for cafe in cafes:
        print(f"  - {cafe['name']}: requires {cafe['points_required']} points, rating {cafe['rating']}/5")
    print("\nSelect a user and click 'Simulate Day' to add a day of steps.")

# 4. Define the button click callback to simulate a day's steps for the selected user [Features 1, 2 & 5]
def on_simulate_click(btn):
    user = user_dropdown.value
    # Simulate a random daily step count (e.g., between 1,000 and 15,000 steps)
    steps_today = random.randint(1000, 15000)
    # Convert steps to points and update the user's totals
    points_earned = steps_today // 1000  # 1 point per 1000 steps
    users[user]['steps'] += steps_today
    users[user]['points'] += points_earned
    # Record the daily steps for the user (to plot progress over multiple simulations)
    users[user].setdefault('daily_steps', []).append(steps_today)
    # Update the output area with new information
    with output_area:
        clear_output()  # clear previous output for a clean update&#8203;:contentReference[oaicite:5]{index=5}
        # Display the simulation result for today
        print(f"📅 {user} walked {steps_today} steps today, earning {points_earned} points.")
        total_steps = users[user]['steps']
        total_points = users[user]['points']
        print(f"🔸 Total steps: {total_steps}  |  Total points: {total_points}")
        # Show a progress bar for today's steps toward a 10k-step goal&#8203;:contentReference[oaicite:6]{index=6}
        goal = 10000
        prog = widgets.IntProgress(
            value=min(steps_today, goal), max=goal, description="Daily", bar_style=""
        )
        display(prog)  # embed the IntProgress bar in output
        # Plot the user's daily steps over time using matplotlib
        fig, ax = plt.subplots(figsize=(4,3))
        ax.plot(users[user]['daily_steps'], marker='o', color='skyblue')
        ax.set_title(f"{user}'s Daily Steps Over Time")
        ax.set_xlabel("Day Count")
        ax.set_ylabel("Steps")
        fig.tight_layout()
        # Display the figure in the output (works because any rich output displays in Output widget)&#8203;:contentReference[oaicite:7]{index=7}
        display(fig)
        plt.close(fig)  # close figure to avoid duplicate output in notebooks
        # Update and display the leaderboard with new points totals
        leaderboard = sorted(users.items(), key=lambda x: x[1]['points'], reverse=True)
        print("\n🏅 Leaderboard (updated):")
        for rank, (uname, data) in enumerate(leaderboard, start=1):
            print(f"  {rank}. {uname} — {data['points']} points")
        # Re-display the partner cafes list (static info)
        print("\n☕ Nearby Partner Cafes:")
        for cafe in cafes:
            print(f"  - {cafe['name']}: requires {cafe['points_required']} points, rating {cafe['rating']}/5")

# 5. Bind the callback to the button and display everything
simulate_btn.on_click(on_simulate_click)
# Display the dropdown, button, and output area in the notebook UI&#8203;:contentReference[oaicite:8]{index=8}
display(user_dropdown, simulate_btn, output_area)
