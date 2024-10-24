import matplotlib.pyplot as plt
import numpy as np

# Define the data
mission_types = ['Planetary Exploration', 'Astronomical Observation', 
                 'Technological Demonstration', 'Human Spaceflight']
mission_counts = [40, 30, 20, 10]

# Additional data for the new subplot
mission_budgets = [300, 250, 150, 100]  # In millions of dollars

# Colors for each mission type
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [1, 1.2]})

# Plot the ring chart in the first subplot
wedges, texts, autotexts = ax1.pie(
    mission_counts,
    labels=mission_types,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    textprops={'fontsize': 10, 'color': 'black'}
)

# Draw a title in the center of the ring
ax1.text(0, 0, 'AstroVentures\nMissions\n2013-2023',
         horizontalalignment='center', verticalalignment='center',
         fontsize=12, fontweight='bold', color='navy')

# Title above the first chart
ax1.set_title("Space Mission Distribution\n(2013-2023)",
              fontsize=14, fontweight='bold', color='navy', pad=20)

# Bar chart in the second subplot for mission budgets
ax2.barh(mission_types, mission_budgets, color=colors, edgecolor='black')
ax2.set_xlabel('Budget in Millions ($)', fontsize=12)
ax2.set_title("Estimated Budget Allocation\nby Mission Type",
              fontsize=14, fontweight='bold', color='navy', pad=20)

# Display the budget values next to the bars
for i, (count, budget) in enumerate(zip(mission_counts, mission_budgets)):
    ax2.text(budget + 5, i, f'${budget}M', va='center', fontsize=10, color='black')

# Adjust layout for both subplots
plt.tight_layout()

# Display the plot
plt.show()