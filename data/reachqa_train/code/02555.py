import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2010, 2021)
satisfaction_scores = np.array([58, 61, 64, 66, 70, 73, 75, 78, 81, 85, 87])
error_margins = np.array([3, 2.5, 3, 2, 2.5, 3, 2, 2.5, 2, 2.5, 3])
brand_releases = np.array([5, 7, 8, 10, 12, 14, 18, 20, 25, 28, 30])

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the line chart with error bars
ax1.errorbar(years, satisfaction_scores, yerr=error_margins, fmt='o-', color='teal',
             ecolor='lightcoral', elinewidth=2, capsize=4, markerfacecolor='darkcyan',
             markeredgewidth=1.5, markersize=6, label='Satisfaction Score')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Satisfaction Score (0 to 100)', fontsize=12, color='teal')
ax1.tick_params(axis='y', labelcolor='teal')

# Secondary y-axis for the bar chart
ax2 = ax1.twinx()
ax2.bar(years, brand_releases, color='orange', alpha=0.5, width=0.5, label='Sustainable Brand Releases')
ax2.set_ylabel('Number of Sustainable Brand Releases', fontsize=12, color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Title and labels
plt.title("The Green Shift: Consumer Attitudes & Brand Evolution\nTowards Sustainable Fashion (2010-2020)", 
          fontsize=16, fontweight='bold', pad=20)

# Adding a grid for clarity
ax1.grid(True, linestyle='--', alpha=0.5)

# Add a legend
fig.legend(loc='upper left', fontsize=12, title='Metrics', bbox_to_anchor=(0.1, 0.85))

# Annotating significant points
ax1.annotate('Major Eco-Friendly Collections\nIntroduced', xy=(2015, 73), xytext=(2012, 78),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=10, color='brown')

ax1.annotate('Post-2018 Awareness Boost', xy=(2018, 81), xytext=(2016, 85),
             arrowprops=dict(facecolor='green', arrowstyle='->', lw=1.5), fontsize=10, color='green')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()