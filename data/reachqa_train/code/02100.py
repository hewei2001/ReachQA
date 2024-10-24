import matplotlib.pyplot as plt
import numpy as np

# Data for Bar Chart: Script names and their usage percentages
scripts = ['Hieroglyphics', 'Cuneiform', 'Runes', 'Sanskrit', 'Mayan Glyphs', 'Chinese Oracle Bone Script']
usage_percentages = [25, 15, 30, 10, 10, 10]

# Data for Pie Chart: Future potential of ancient scripts
future_potential = [20, 25, 15, 10, 20, 10]

# Define distinct colors for each script
colors = ['#FFD700', '#8B4513', '#8B008B', '#4682B4', '#FF8C00', '#32CD32']

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(18, 8), gridspec_kw={'width_ratios': [2, 1]})

# Plot the horizontal bar chart
bars = ax1.barh(scripts, usage_percentages, color=colors, edgecolor='black', height=0.6)

# Annotate each bar with the usage percentage
for bar in bars:
    ax1.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
             f'{bar.get_width()}%', va='center', ha='left', fontsize=10, color='black')

# Title and axis labels for bar chart
ax1.set_title('The Renaissance of Ancient Scripts:\nModern Usage in Creative Projects', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Usage Percentage (%)', fontsize=12)
ax1.set_ylabel('Ancient Scripts', fontsize=12)

# Customize y-axis to ensure script names align with bars
ax1.set_yticks(np.arange(len(scripts)))
ax1.set_yticklabels(scripts, fontsize=12)

# Add grid lines to aid readability
ax1.grid(axis='x', linestyle='--', alpha=0.7)

# Plot the pie chart
ax2.pie(future_potential, labels=scripts, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops={'edgecolor': 'black'})
ax2.set_title('Future Potential of Ancient Scripts', fontsize=14, weight='bold', pad=20)

# Adjust layout to ensure no overlap and better alignment
plt.tight_layout()

# Display the plot
plt.show()