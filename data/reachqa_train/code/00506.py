import matplotlib.pyplot as plt
import numpy as np

# Data
centuries = ['15th Century', '16th Century', '17th Century', '18th Century', '19th Century', '20th Century']
artifacts_discovered = [50, 75, 120, 160, 200, 180]
artifact_value_estimates = [200, 350, 450, 600, 750, 710]  # In arbitrary units

# Setting up the figure and primary axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart for artifacts discovered
bars = ax1.bar(centuries, artifacts_discovered, color=['#b3cde0', '#6497b1', '#005b96', '#03396c', '#011f4b', '#051e3e'])

# Line plot for artifact value estimates
ax2 = ax1.twinx()
ax2.plot(centuries, artifact_value_estimates, color='orange', marker='o', linestyle='--', linewidth=2, label='Value Estimate')

# Titles and labels
ax1.set_title('Artifact Discoveries and Estimated Values by Century\nExploring Historical Significance', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Century', fontsize=12)
ax1.set_ylabel('Number of Artifacts Discovered', fontsize=12)
ax2.set_ylabel('Estimated Value (units)', fontsize=12, color='orange')

# Annotating each bar with the number of discoveries
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 3, int(yval), ha='center', va='bottom', fontsize=10)

# Adding trend line annotations for the line plot
for i, value in enumerate(artifact_value_estimates):
    ax2.text(i, value, f'{value}', color='orange', fontsize=10, ha='center', va='bottom')

# Gridlines and ticks
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
plt.xticks(rotation=45, ha='right')

# Legends
ax1.legend(['Discoveries per Century'], loc='upper left', frameon=False)
ax2.legend(loc='upper right', frameon=False)

# Adjust layout
plt.tight_layout()

# Display plot
plt.show()