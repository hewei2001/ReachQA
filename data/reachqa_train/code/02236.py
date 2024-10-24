import matplotlib.pyplot as plt
import numpy as np

# Data for renewable energy adoption by country
countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']
renewable_percentages = [82, 75, 68, 63, 58]

# Define bar colors
colors = ['#4CAF50', '#2196F3', '#FFEB3B', '#FFC107', '#FF5722']

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Create bar chart with positions and colors
bar_positions = np.arange(len(countries))
bars = ax.bar(bar_positions, renewable_percentages, color=colors, width=0.5)

# Title and labels
ax.set_title('Leading Countries in Renewable Energy Adoption\n(2023)', fontsize=16, fontweight='bold')
ax.set_xlabel('Country', fontsize=12)
ax.set_ylabel('Percentage of Energy from Renewable Sources (%)', fontsize=12)
ax.set_xticks(bar_positions)
ax.set_xticklabels(countries)
ax.set_ylim(0, 100)

# Annotate each bar with the percentage value
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%', 
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), 
                textcoords='offset points',
                ha='center', va='bottom',
                fontsize=11, color='black', weight='bold')

# Add grid lines for y-axis
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Remove x-axis grid lines
ax.grid(axis='x', linestyle='')

# Automatically adjust the layout to prevent text from being clipped
plt.tight_layout()

# Show the plot
plt.show()