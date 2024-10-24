import matplotlib.pyplot as plt
import numpy as np

# Months in 2023 for the analysis
months = ['January', 'February', 'March', 'April', 'May', 'June']
indices = np.arange(len(months))

# Daily active players (in thousands) for each game genre over the six months
moba_players = np.array([500, 520, 540, 580, 620, 660])
fps_players = np.array([400, 420, 430, 450, 470, 490])
rpg_players = np.array([300, 350, 370, 390, 410, 430])

# Monthly revenue in millions for each genre
moba_revenue = np.array([50, 55, 60, 70, 75, 80])
fps_revenue = np.array([35, 38, 40, 45, 50, 55])
rpg_revenue = np.array([25, 30, 35, 40, 45, 50])

# Create the figure and axis objects
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the player data
ax1.plot(months, moba_players, marker='o', linestyle='-', label='MOBA Players', color='#FF6347', linewidth=2)
ax1.plot(months, fps_players, marker='v', linestyle='--', label='FPS Players', color='#4682B4', linewidth=2)
ax1.plot(months, rpg_players, marker='s', linestyle='-.', label='RPG Players', color='#32CD32', linewidth=2)

# Annotate significant points
ax1.annotate('Major Content Update', xy=('April', 580), xytext=('February', 620),
             arrowprops=dict(facecolor='black', shrink=0.05, headwidth=8, width=2),
             fontsize=10, ha='center', fontstyle='italic', color='#FF6347')

ax1.annotate('Summer Sale Event', xy=('June', 490), xytext=('April', 470),
             arrowprops=dict(facecolor='black', shrink=0.05, headwidth=8, width=2),
             fontsize=10, ha='center', fontstyle='italic', color='#4682B4')

ax1.annotate('New Game Release', xy=('March', 370), xytext=('January', 410),
             arrowprops=dict(facecolor='black', shrink=0.05, headwidth=8, width=2),
             fontsize=10, ha='center', fontstyle='italic', color='#32CD32')

# Label each data point with its value
for month, moba, fps, rpg in zip(months, moba_players, fps_players, rpg_players):
    ax1.text(month, moba + 10, f'{moba}', color='#FF6347', ha='center', va='bottom', fontsize=9)
    ax1.text(month, fps + 10, f'{fps}', color='#4682B4', ha='center', va='bottom', fontsize=9)
    ax1.text(month, rpg + 10, f'{rpg}', color='#32CD32', ha='center', va='bottom', fontsize=9)

# Set title and labels for the first axis
ax1.set_title("Popularity and Revenue Dynamics of Digital Games in 2023", fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel("Months in 2023", fontsize=12)
ax1.set_ylabel("Daily Active Players (in thousands)", fontsize=12)
ax1.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Create a secondary y-axis for revenue
ax2 = ax1.twinx()
bar_width = 0.25

# Plotting the revenue data as a bar chart
ax2.bar(indices - bar_width, moba_revenue, bar_width, label='MOBA Revenue', color='#FF6347', alpha=0.5)
ax2.bar(indices, fps_revenue, bar_width, label='FPS Revenue', color='#4682B4', alpha=0.5)
ax2.bar(indices + bar_width, rpg_revenue, bar_width, label='RPG Revenue', color='#32CD32', alpha=0.5)

ax2.set_ylabel("Monthly Revenue (in millions)", fontsize=12)

# Add legends for both plots
lines_labels = ax1.get_legend_handles_labels()
bars_labels = ax2.get_legend_handles_labels()
ax1.legend(lines_labels[0] + bars_labels[0], lines_labels[1] + bars_labels[1], loc='upper left', fontsize=10, frameon=True)

# Ensure layout is adjusted
plt.tight_layout()

# Display the plot
plt.show()