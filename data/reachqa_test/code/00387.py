import matplotlib.pyplot as plt
import numpy as np

# Game titles
games = [
    'Dota 2',
    'League of Legends',
    'Fortnite',
    'PlayerUnknown\'s Battlegrounds',
    'Overwatch',
    'Apex Legends',
    'Hearthstone',
    'StarCraft II',
    'Street Fighter V',
    'CS:GO'
]

# Prize pool values (in millions of USD)
prize_pools = [
    40.2,
    22.1,
    20.5,
    18.3,
    15.6,
    12.8,
    10.2,
    9.5,
    8.3,
    7.2
]

# Viewership data (in millions)
viewership = [
    1.2,
    1.5,
    1.1,
    0.9,
    0.8,
    0.7,
    0.6,
    0.5,
    0.4,
    0.3
]

# Create a new figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create the bar chart
x = np.arange(len(games))
width = 0.6
ax.bar(x, prize_pools, width, color='#66b3ff', alpha=0.8, label='Prize Pool')

# Add data annotations above the bars
for i, prize_pool in enumerate(prize_pools):
    ax.text(i, prize_pool + 1, f'{prize_pool:.1f}M', ha='center', va='bottom', fontsize=10)

# Create the line chart for viewership
ax.plot(x, viewership, color='#ff9999', marker='o', linestyle='-', linewidth=2, label='Viewership')

# Add data annotations for viewership
for i, viewers in enumerate(viewership):
    ax.text(i, viewers + 0.1, f'{viewers:.1f}M', ha='center', va='bottom', fontsize=10)

# Customize the chart
ax.set_title('The Rise of E-Sports: Top 10 Games by Prize Pool (2022)\n'
             'Prize Pools and Viewership in Millions of USD')
ax.set_xlabel('Game')
ax.set_ylabel('Prize Pool (millions of USD)')
ax.set_xticks(x)
ax.set_xticklabels(games, rotation=45, ha='right', fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(loc='upper right', fontsize=10)

# Layout adjustments
fig.tight_layout(rect=[0, 0, 0.85, 0.95])

# Show the plot
plt.show()