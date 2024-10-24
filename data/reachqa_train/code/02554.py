import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2010, 2021)
satisfaction_scores = np.array([58, 61, 64, 66, 70, 73, 75, 78, 81, 85, 87])
error_margins = np.array([3, 2.5, 3, 2, 2.5, 3, 2, 2.5, 2, 2.5, 3])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the line chart with error bars
ax.errorbar(years, satisfaction_scores, yerr=error_margins, fmt='o-', color='teal', 
            ecolor='lightcoral', elinewidth=2, capsize=4, markerfacecolor='darkcyan', 
            markeredgewidth=1.5, markersize=6, label='Satisfaction Score')

# Title and axis labels
ax.set_title("The Green Shift: Consumer Attitudes Towards\nSustainable Fashion (2010-2020)", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Satisfaction Score (0 to 100)', fontsize=12)

# Add grid for readability
ax.grid(True, linestyle='--', alpha=0.5)

# Adding a legend
ax.legend(loc='upper left', fontsize=12, title='Metric')

# Annotating significant points
ax.annotate('Major Eco-Friendly Collections\nIntroduced', xy=(2015, 73), xytext=(2012, 78),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=10, color='brown')

ax.annotate('Post-2018 Awareness Boost', xy=(2018, 81), xytext=(2016, 85),
            arrowprops=dict(facecolor='green', arrowstyle='->', lw=1.5), fontsize=10, color='green')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()