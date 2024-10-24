import matplotlib.pyplot as plt
import numpy as np

# Define spells and their usage frequency
spells = ["Lumos", "Alohomora", "Expelliarmus", "Accio", 
          "Wingardium Leviosa", "Expecto Patronum", "Riddikulus"]
usage_frequency = [1200, 950, 800, 600, 850, 400, 450]

# Color palette for each spell
colors = ['#FFD700', '#FF4500', '#ADFF2F', '#00BFFF', '#BA55D3', '#8A2BE2', '#FF6347']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the vertical bar chart
bars = ax.bar(spells, usage_frequency, color=colors, edgecolor='black', width=0.6)

# Add data labels above each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 20,
            f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

# Customize the appearance
ax.set_ylabel('Usage Frequency', fontsize=12, fontweight='bold')
ax.set_title('Popular Magical Spells in the Wizarding World\nAnnual Usage Statistics',
             fontsize=16, fontweight='bold', pad=20)
ax.set_ylim(0, max(usage_frequency) + 100)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Set tick labels with appropriate alignment
ax.set_xticks(np.arange(len(spells)))
ax.set_xticklabels(spells, fontsize=11, weight='bold', rotation=45, ha='right')

# Adjust layout to ensure the chart is visually appealing
plt.tight_layout()

# Display the plot
plt.show()