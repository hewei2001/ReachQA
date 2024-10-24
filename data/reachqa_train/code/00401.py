import matplotlib.pyplot as plt
import numpy as np

# Platforms and their usage percentages across different age groups
platforms = ['Streamify', 'TuneBox', 'HarmoNet', 'BeatSphere', 'NoteCloud']
usage_teens = [35, 25, 15, 15, 10]
usage_young_adults = [30, 20, 25, 15, 10]
usage_adults = [20, 25, 20, 25, 10]
usage_seniors = [10, 15, 25, 30, 20]

# Data preparation for percentage bar chart
age_groups = [usage_teens, usage_young_adults, usage_adults, usage_seniors]
age_labels = ['Teens (13-19)', 'Young Adults (20-29)', 'Adults (30-49)', 'Seniors (50+)']

# Set colors for each platform
colors = ['#4daf4a', '#377eb8', '#ff7f00', '#f781bf', '#984ea3']

# Create figure and axes for plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Initialize the bottom array for stacking
bottom = np.zeros(len(age_labels))

# Plot the percentage bar chart
for i, (platform, color) in enumerate(zip(platforms, colors)):
    percentages = [group[i] for group in age_groups]
    ax.bar(age_labels, percentages, bottom=bottom, label=platform, color=color, alpha=0.8)
    
    # Add percentage labels to each segment
    for j, val in enumerate(percentages):
        ax.text(j, bottom[j] + val / 2, f'{val}%', ha='center', va='center', fontsize=10, color='white')
    
    # Update the bottom array for next stack
    bottom += percentages

# Setting a consistent y-axis range for percentage representation
ax.set_ylim(0, 100)

# Adding titles and labels
ax.set_title('Percentage Usage of Music Streaming Services\nAcross Age Groups in Technopolis',
             fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Percentage of Usage (%)', fontsize=14)
ax.set_xlabel('Age Groups', fontsize=14)

# Customize the legend for platform colors
ax.legend(title='Platforms', title_fontsize='13', fontsize='11', loc='upper right')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()