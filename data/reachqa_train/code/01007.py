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

# Satisfaction scores for each decade
satisfaction_scores = np.array([70, 75, 85])

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(12, 8))

# Stacked area plot
ax1.stackplot(decades, data, labels=['Adventure Travel', 'Cultural Travel', 'Relaxation Travel', 'Business Travel'],
              colors=colors, alpha=0.8)
ax1.set_xlabel('Decade', fontsize=14, weight='bold', labelpad=10)
ax1.set_ylabel('Percentage Share of Travel Type', fontsize=14, weight='bold', labelpad=10)

# Adding grid lines for clarity
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.set_yticks(np.arange(0, 101, 10))
ax1.set_yticklabels([f'{y}%' for y in np.arange(0, 101, 10)], fontsize=12)

# Remove unnecessary spines
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Legend configuration for area plot
ax1.legend(loc='upper left', fontsize=12, title='Travel Categories', title_fontsize='13', bbox_to_anchor=(1, 1))

# Overlay line plot for satisfaction scores
ax2 = ax1.twinx()
ax2.plot(decades, satisfaction_scores, color='purple', marker='o', linestyle='--', linewidth=2, markersize=8, label='Avg. Satisfaction Score')
ax2.set_ylabel('Average Satisfaction Score', fontsize=14, weight='bold', labelpad=10)
ax2.set_ylim(0, 100)  # Assuming scores are percentages for consistency
ax2.set_yticks(np.arange(0, 101, 10))
ax2.set_yticklabels([f'{y}%' for y in np.arange(0, 101, 10)], fontsize=12)

# Additional Legend for line plot
ax2.legend(loc='upper right', fontsize=12, title='Additional Metrics', title_fontsize='13', bbox_to_anchor=(1, 0.98))

# Title with a line break for clarity
ax1.set_title('Evolution of Travel Preferences Across Decades\nwith Average Satisfaction Scores',
              fontsize=18, weight='bold', pad=20)

# Automatically adjust layout for clarity
plt.tight_layout()

# Show the plot
plt.show()