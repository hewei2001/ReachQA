import matplotlib.pyplot as plt
import numpy as np

# Hypothetical average monthly sunshine hours for each city
sunshine_data = {
    "San Francisco": [160, 155, 180, 210, 240, 280, 300, 310, 270, 230, 180, 160],
    "Cairo": [300, 290, 310, 310, 340, 360, 380, 370, 350, 330, 310, 300],
    "Mumbai": [250, 230, 220, 180, 160, 150, 160, 170, 180, 210, 230, 250],
    "Sydney": [220, 200, 190, 180, 160, 160, 170, 200, 210, 220, 230, 240],
    "Tokyo": [180, 160, 170, 180, 200, 220, 240, 230, 220, 190, 180, 170]
}

# Extract the data for plotting
cities = list(sunshine_data.keys())
sunshine_hours = list(sunshine_data.values())

# Calculate total yearly sunshine hours for each city
yearly_sunshine_hours = [sum(hours) for hours in sunshine_hours]

# Create the figure and the subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 7))

# First subplot - Box Plot
axes[0].boxplot(sunshine_hours, vert=True, patch_artist=True, notch=True, labels=cities,
                boxprops=dict(facecolor='lightblue', color='blue', alpha=0.7),
                whiskerprops=dict(color='blue'),
                capprops=dict(color='blue'),
                medianprops=dict(color='darkred'),
                flierprops=dict(markerfacecolor='red', marker='o', markersize=5, linestyle='none', alpha=0.5))
axes[0].set_title("Monthly Sunshine Hours Distribution\nAcross Five Cities", fontsize=12, weight='bold')
axes[0].set_ylabel("Average Monthly Sunshine Hours", fontsize=10)
axes[0].set_xlabel("Cities", fontsize=10)
axes[0].yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Second subplot - Bar Plot for Total Annual Sunshine
axes[1].bar(cities, yearly_sunshine_hours, color='skyblue', edgecolor='blue', alpha=0.7)
axes[1].set_title("Total Annual Sunshine Hours\nFor Each City", fontsize=12, weight='bold')
axes[1].set_ylabel("Total Yearly Sunshine Hours", fontsize=10)
axes[1].set_xlabel("Cities", fontsize=10)
for i, v in enumerate(yearly_sunshine_hours):
    axes[1].text(i, v + 20, str(v), ha='center', va='bottom', fontsize=9, fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()