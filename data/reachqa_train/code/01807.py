import matplotlib.pyplot as plt
import numpy as np

# Define the architectural styles and their corresponding percentages
styles = ['Modern', 'Victorian', 'Art Deco', 'Colonial', 'Mediterranean', 'Gothic Revival', 'Brutalist']
percentages = np.array([35, 20, 15, 10, 10, 5, 5])

# Define colors for each architectural style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(styles, percentages, color=colors, edgecolor='black')

# Add data labels beside each bar
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%', xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0), textcoords="offset points", ha='left', va='center', fontsize=11, fontweight='bold')

# Set the title with multiple lines for readability
ax.set_title('Architectural Style Distribution in\nUrban Residential Buildings of Archville - 2023',
             fontsize=16, fontweight='bold', pad=20)

# Set labels for the axes
ax.set_xlabel('Percentage of Total Residential Buildings', fontsize=12)

# Configure x-axis to show percentage from 0 to 100
ax.set_xlim(0, 100)
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))

# Hide y-axis grid lines and show x-axis grid lines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.yaxis.grid(False)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()