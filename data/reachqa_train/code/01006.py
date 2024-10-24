import matplotlib.pyplot as plt
import numpy as np

# Decades for the x-axis
decades = ['1980s', '2000s', '2020s']

# Data for travel types over the decades
adventure = np.array([10, 20, 30])
cultural = np.array([30, 30, 25])
relaxation = np.array([40, 35, 40])
business = np.array([20, 15, 5])

# Stack the data
data = np.vstack([adventure, cultural, relaxation, business])

# Color configuration for the layers
colors = ['#ffcc99', '#99ff99', '#66b3ff', '#ff9999']

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked area plot
ax.stackplot(decades, data, labels=['Adventure Travel', 'Cultural Travel', 'Relaxation Travel', 'Business Travel'], colors=colors, alpha=0.8)

# Title and labels
ax.set_title('Evolution of Travel Preferences\nAcross Decades', fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=14, weight='bold', labelpad=10)
ax.set_ylabel('Percentage Share of Travel Type', fontsize=14, weight='bold', labelpad=10)

# Legend configuration
ax.legend(loc='upper left', fontsize=12, title='Travel Categories', title_fontsize='13', bbox_to_anchor=(1, 1))

# Adding grid lines for clarity
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Set yticks with percentage labels
ax.set_yticks(np.arange(0, 101, 10))
ax.set_yticklabels([f'{y}%' for y in np.arange(0, 101, 10)], fontsize=12)

# Set x-ticks without rotation since they are short
ax.set_xticks(decades)

# Remove unnecessary spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()