import matplotlib.pyplot as plt
import numpy as np

# Define the years and mock average scores with standard deviation
years = np.arange(2010, 2020)
average_scores = [75, 77, 76, 78, 79, 80, 82, 81, 83, 85]
score_std_dev = [3, 2, 4, 3, 5, 3, 4, 2, 3, 4]

# Creating the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the line chart with error bars
ax.errorbar(
    years, average_scores, yerr=score_std_dev, fmt='-o', color='navy',
    ecolor='orange', elinewidth=2, capsize=5, capthick=2, markerfacecolor='white',
    label='Average Mathematics Score'
)

# Adding plot details
ax.set_title('Evolution of Student Performance\nin Mathematics Over a Decade', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Score', fontsize=12)
ax.set_xticks(years)
ax.set_yticks(np.arange(70, 90, 2))
ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.5)
ax.legend(loc='upper left', fontsize=10)

# Annotation for key insights
ax.annotate(
    'New Curriculum Introduced', xy=(2014, 79), xytext=(2011, 83),
    arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred'
)

# Setting limits for better visualization
ax.set_xlim(2009, 2020)
ax.set_ylim(70, 88)

# Final layout adjustment and display
plt.tight_layout()
plt.show()