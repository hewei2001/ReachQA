import matplotlib.pyplot as plt
import numpy as np

# Months in 2023 for the analysis
months = ['January', 'February', 'March', 'April', 'May', 'June']

# Daily active players (in thousands) for each game genre over the six months
moba_players = np.array([500, 520, 540, 580, 620, 660])
fps_players = np.array([400, 420, 430, 450, 470, 490])
rpg_players = np.array([300, 350, 370, 390, 410, 430])

# Create the line chart
plt.figure(figsize=(12, 7))

# Plotting the data
plt.plot(months, moba_players, marker='o', linestyle='-', label='MOBA Games', color='#FF6347', linewidth=2)
plt.plot(months, fps_players, marker='v', linestyle='--', label='FPS Games', color='#4682B4', linewidth=2)
plt.plot(months, rpg_players, marker='s', linestyle='-.', label='RPG Games', color='#32CD32', linewidth=2)

# Annotating significant points
plt.annotate('Major Content Update', xy=('April', 580), xytext=('February', 620),
             arrowprops=dict(facecolor='black', shrink=0.05, headwidth=8, width=2),
             fontsize=10, ha='center', fontstyle='italic', color='#FF6347')

plt.annotate('Summer Sale Event', xy=('June', 490), xytext=('April', 470),
             arrowprops=dict(facecolor='black', shrink=0.05, headwidth=8, width=2),
             fontsize=10, ha='center', fontstyle='italic', color='#4682B4')

plt.annotate('New Game Release', xy=('March', 370), xytext=('January', 410),
             arrowprops=dict(facecolor='black', shrink=0.05, headwidth=8, width=2),
             fontsize=10, ha='center', fontstyle='italic', color='#32CD32')

# Label each data point with its value
for month, moba, fps, rpg in zip(months, moba_players, fps_players, rpg_players):
    plt.text(month, moba + 10, f'{moba}', color='#FF6347', ha='center', va='bottom', fontsize=9)
    plt.text(month, fps + 10, f'{fps}', color='#4682B4', ha='center', va='bottom', fontsize=9)
    plt.text(month, rpg + 10, f'{rpg}', color='#32CD32', ha='center', va='bottom', fontsize=9)

# Add titles and labels
plt.title("Popularity Surge of Digital Games Post-Pandemic\nA Comparative Analysis", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Months in 2023", fontsize=12)
plt.ylabel("Daily Active Players (in thousands)", fontsize=12)

# Add a legend
plt.legend(loc='upper left', fontsize=10, frameon=True)

# Enhance grid for readability
plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust layout to ensure readability
plt.tight_layout()

# Display the plot
plt.show()