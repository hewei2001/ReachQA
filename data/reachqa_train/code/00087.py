import matplotlib.pyplot as plt
import numpy as np

# Data: Projected Energy Mix in 2050
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Nuclear', 'Coal', 'Natural Gas', 'Other Renewables']
percentages = [25, 20, 15, 10, 10, 15, 5]

# Plotting the percentage bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Create a horizontal bar chart
bars = ax.barh(energy_sources, percentages, color=['#FFD700', '#1E90FF', '#32CD32', '#FFA07A', '#A9A9A9', '#FF4500', '#9370DB'])

# Add grid lines for better readability
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Label each bar with the percentage value
ax.bar_label(bars, fmt='%.1f%%')

# Set the title and labels
ax.set_title('Projected Global Energy Source Composition\nfor Sustainability in 2050', fontsize=16, pad=20)
ax.set_xlabel('Percentage of Total Energy Consumption', fontsize=12)
ax.set_xlim(0, 30)

# Customize the y-axis for better visual alignment
ax.set_yticklabels(energy_sources, fontsize=11)

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()