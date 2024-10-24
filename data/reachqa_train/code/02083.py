import matplotlib.pyplot as plt
import numpy as np

# Data: Countries and their renewable energy adoption percentages
countries = ['Norway', 'Germany', 'China', 'United States', 'India', 'Brazil', 'Spain', 'Australia', 'Japan', 'South Africa']
renewable_percentages = [98, 48, 35, 20, 28, 83, 45, 41, 25, 18]

# Colors for each country using shades of green
colors = plt.cm.Greens(np.linspace(0.4, 0.9, len(countries)))

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.barh(countries, renewable_percentages, color=colors, edgecolor='black', height=0.6)

# Title and axis labels
ax.set_title('Renewable Energy Adoption by Country\nin 2023', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Percentage of Energy from Renewables (%)', fontsize=12)

# Label each bar with the percentage value
ax.bar_label(bars, fmt='%.0f%%', padding=3, fontsize=11)

# Set x-axis limits to cover full 0-100% range
ax.set_xlim(0, 100)

# Align y-axis category labels
ax.set_yticks(np.arange(len(countries)))
ax.set_yticklabels(countries, fontsize=12)

# Add grid lines for easier value estimation
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Adjust layout to prevent any text overlap
plt.tight_layout()

# Display the chart
plt.show()