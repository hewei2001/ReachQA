import matplotlib.pyplot as plt
import numpy as np

# Define countries and their cumulative investment in renewable energy from 2010 to 2022 (in billion dollars)
countries = np.array(['China', 'USA', 'Germany', 'India', 'Brazil', 'Australia'])
investments = np.array([950, 820, 460, 330, 290, 210])

# Generate the horizontal bar chart
fig, ax = plt.subplots(figsize=(14, 8))

# Customize bar colors using a color map
colors = plt.cm.viridis(np.linspace(0, 1, len(countries)))

# Create horizontal bars
bars = ax.barh(countries, investments, color=colors, edgecolor='darkgrey')

# Set title and labels with proper alignment
ax.set_title("Global Renewable Energy Investments (2010-2022)\nLeading Countries' Contributions", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Cumulative Investment (Billion Dollars)', fontsize=14)
ax.set_ylabel('Countries', fontsize=14)

# Add data labels to each bar
for bar in bars:
    width = bar.get_width()
    ax.text(width + 20, bar.get_y() + bar.get_height()/2, f'{width:.0f}B', va='center', ha='center', color='black', fontsize=12)

# Customize the x-axis
ax.set_xlim(0, 1050)  # Extend the x-limit to make room for labels
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}B'))

# Add vertical gridlines for improved readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()