import matplotlib.pyplot as plt
import numpy as np

# Fixed data with 8 data points per category
gaming_hours = [2, 3, 4, 5, 6, 5, 7, 8]
social_media_hours = [1, 2, 2, 3, 3, 4, 2, 5]
educational_hours = [1, 1, 2, 1, 3, 2, 2, 3]
streaming_hours = [1, 2, 3, 3, 3, 4, 3, 4]
fitness_hours = [0, 1, 1, 2, 2, 1, 1, 2]

# Additional data for the new subplot: Total weekly hours per category
total_weekly_hours = [sum(gaming_hours), sum(social_media_hours), sum(educational_hours), 
                      sum(streaming_hours), sum(fitness_hours)]

categories = ['Gaming', 'Social Media', 'Educational', 'Streaming', 'Fitness']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create a figure with 2 subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Plot the original histogram with fixed data and aligned bars
bins = np.arange(0, 9, 1)
axs[0].hist([gaming_hours, social_media_hours, educational_hours, streaming_hours, fitness_hours],
            bins=bins, color=colors, alpha=0.7, rwidth=0.75, align='left', label=categories)

axs[0].set_title('Distribution of Daily Screen Time Among Teens\nfor Various Mobile App Categories', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Hours per Day', fontsize=12)
axs[0].set_ylabel('Number of Teens', fontsize=12)
axs[0].legend(title='App Category', fontsize=10)
axs[0].grid(axis='y', alpha=0.75, linestyle='--', linewidth=0.5)
axs[0].set_xticks(bins)
axs[0].xaxis.set_tick_params(labelsize=10)
axs[0].yaxis.set_tick_params(labelsize=10)

# New plot: Bar chart of total weekly hours spent on each category
axs[1].bar(categories, total_weekly_hours, color=colors, alpha=0.8)
axs[1].set_title('Total Weekly Screen Time per App Category', fontsize=14, fontweight='bold')
axs[1].set_xlabel('App Category', fontsize=12)
axs[1].set_ylabel('Total Hours per Week', fontsize=12)
axs[1].yaxis.set_tick_params(labelsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()