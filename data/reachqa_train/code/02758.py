import matplotlib.pyplot as plt
import numpy as np

# Define project names
projects = ['Mars Colonization', 'Asteroid Mining', 'Space Telescope Development', 
            'Lunar Research', 'Exoplanet Discovery']

# Data: Percentage and actual budget allocations for each project
budget_percentages = [30, 25, 20, 15, 10]  # Sum = 100%
budget_amounts = [300, 250, 200, 150, 100]  # In million dollars

# Colors for each project segment
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create figure and subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 8))

# Donut Chart for Budget Percentages
wedges, texts, autotexts = ax[0].pie(budget_percentages, 
                                     labels=projects, 
                                     colors=colors, 
                                     autopct='%1.1f%%',
                                     startangle=90, 
                                     pctdistance=0.85,
                                     wedgeprops=dict(width=0.3),
                                     explode=(0.05, 0, 0, 0, 0),
                                     shadow=True)

# Customize percentage text inside pie slices
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)

# Add a circle at the center to create a donut chart effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax[0].add_artist(centre_circle)

# Set aspect ratio to be equal to maintain the circular shape
ax[0].set_aspect('equal')  

# Title for the donut chart
ax[0].set_title('Percentage of IRA 2023 Budget Allocations\nfor Strategic Space Projects', 
                fontsize=14, fontweight='bold', pad=20)

# Horizontal Bar Chart for Actual Budget Amounts
y_pos = np.arange(len(projects))
ax[1].barh(y_pos, budget_amounts, color=colors, edgecolor='black')
ax[1].set_yticks(y_pos)
ax[1].set_yticklabels(projects)
ax[1].invert_yaxis()  # Reverse the order of projects

# Labeling and annotations
ax[1].set_xlabel('Budget in Million Dollars', fontsize=12)
for index, value in enumerate(budget_amounts):
    ax[1].text(value + 5, index, f'{value}M', va='center', ha='left', fontsize=10)

# Title for the bar chart
ax[1].set_title('IRA 2023 Project Budgets\nin Million Dollars', 
                fontsize=14, fontweight='bold', pad=20)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()