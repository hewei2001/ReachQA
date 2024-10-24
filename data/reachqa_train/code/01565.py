import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

# Define the years and mission types
years = np.arange(1980, 2025, 5)
mission_types = ['Orbital', 'Lunar', 'Martian', 'Deep Space', 'Crew Missions']

# Create data representing the percentage focus on each mission type
orbital = np.array([70, 65, 60, 55, 50, 45, 40, 35, 30])
lunar = np.array([10, 10, 10, 12, 15, 15, 20, 20, 25])
martian = np.array([5, 5, 8, 10, 10, 15, 15, 18, 20])
deep_space = np.array([5, 7, 7, 8, 10, 12, 15, 15, 15])
crew_missions = 100 - (orbital + lunar + martian + deep_space)

# Create the figure and axis for the percentage bar chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plot data using stacked bar chart with added 3D effect
bar_width = 4
ax.bar(years, orbital, label=mission_types[0], width=bar_width, color='#1f77b4', edgecolor='grey', linewidth=1.5)
ax.bar(years, lunar, bottom=orbital, label=mission_types[1], width=bar_width, color='#ff7f0e', edgecolor='grey', linewidth=1.5)
ax.bar(years, martian, bottom=orbital + lunar, label=mission_types[2], width=bar_width, color='#2ca02c', edgecolor='grey', linewidth=1.5)
ax.bar(years, deep_space, bottom=orbital + lunar + martian, label=mission_types[3], width=bar_width, color='#d62728', edgecolor='grey', linewidth=1.5)
ax.bar(years, crew_missions, bottom=orbital + lunar + martian + deep_space, label=mission_types[4], width=bar_width, color='#9467bd', edgecolor='grey', linewidth=1.5)

# Title and labels with enhanced styling
ax.set_title("Evolution of Space Exploration Missions\nShift in Focus Among Different Mission Types (1980-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=14, fontweight='semibold')
ax.set_ylabel("Percentage Focus (%)", fontsize=14, fontweight='semibold')

# Legend configuration outside plot area for clarity
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Mission Types', fontsize=11)

# Set y-axis to percentage format and limit
ax.set_yticks(np.arange(0, 101, 10))
ax.set_yticklabels([f"{i}%" for i in range(0, 101, 10)])

# Highlight notable transitions with enhanced annotations
annotated_years = {1995: "Rise of Lunar Missions", 2010: "Increase in Martian Focus", 2020: "Deep Space Priority"}
for year, label in annotated_years.items():
    ax.annotate(label, xy=(year, 60), xytext=(year - 5, 80),
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='white'),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Directly label each segment with its percentage value
for i, year in enumerate(years):
    cumulative = 0
    for j, (percent, color) in enumerate(zip([orbital[i], lunar[i], martian[i], deep_space[i], crew_missions[i]], 
                                             ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])):
        if percent > 5:  # Only label segments large enough to read
            ax.text(year, cumulative + percent / 2, f'{percent}%', color='white', ha='center', va='center', fontsize=10, fontweight='bold')
        cumulative += percent

# Add subtle vertical grid lines
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Apply a contrasting theme background
fig.patch.set_facecolor('#f0f0f0')
ax.set_facecolor('#eaeaf2')

# Automatically adjust the layout for optimal viewing
plt.tight_layout()

# Display the plot
plt.show()