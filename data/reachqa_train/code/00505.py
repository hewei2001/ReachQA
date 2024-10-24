import matplotlib.pyplot as plt
import numpy as np

# Centuries from 15th to 20th
centuries = ['15th Century', '16th Century', '17th Century', '18th Century', '19th Century', '20th Century']

# Number of artifacts discovered from each century (manually crafted for the storyline)
artifacts_discovered = [50, 75, 120, 160, 200, 180]

# Setting up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the histogram as a bar chart
bars = ax.bar(centuries, artifacts_discovered, color=['#b3cde0', '#6497b1', '#005b96', '#03396c', '#011f4b', '#051e3e'])

# Customizing the chart
ax.set_title('Artifact Discoveries by Century\nA Journey Through Time', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Century', fontsize=12)
ax.set_ylabel('Number of Artifacts Discovered', fontsize=12)

# Annotating each bar with the number of discoveries
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 3, int(yval), ha='center', va='bottom', fontsize=10)

# Adding grid lines for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Customizing x-tick labels for better readability
plt.xticks(rotation=45, ha='right')

# Adding a legend to explain the chart
plt.legend(['Discoveries per Century'], loc='upper left', frameon=False)

# Automatically adjusting layout to prevent overlap
plt.tight_layout()

# Displaying the plot
plt.show()