import matplotlib.pyplot as plt
import numpy as np

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Artificial usage data (in hours) for three apps across the week
fittrack_usage = [2, 2.5, 2.7, 3, 3.5, 4, 4.5]
mindspace_usage = [1, 1.2, 1.3, 1.5, 2, 2.2, 2.8]
photosnap_usage = [2, 2.3, 2.8, 3.2, 3.5, 4, 5]

# Calculate cumulative usage for stacked plotting
mindspace_cumulative = mindspace_usage
fittrack_cumulative = np.array(mindspace_usage) + np.array(fittrack_usage)
total_usage = np.array(mindspace_usage) + np.array(fittrack_usage) + np.array(photosnap_usage)

# Plot configuration
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the area chart
ax.fill_between(days, mindspace_cumulative, color='skyblue', alpha=0.7, label='MindSpace')
ax.fill_between(days, fittrack_cumulative, mindspace_cumulative, color='lightgreen', alpha=0.7, label='FitTrack')
ax.fill_between(days, total_usage, fittrack_cumulative, color='salmon', alpha=0.7, label='PhotoSnap')

# Titles and labels
ax.set_title('Weekly Engagement Patterns in Mobile Apps', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Days of the Week', fontsize=12)
ax.set_ylabel('Hours of Usage', fontsize=12)

# Adding a legend
ax.legend(loc='upper left', title='Apps', fontsize=10, frameon=False)

# Enhance visual details
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
ax.set_ylim(0, 15)
ax.set_yticks(range(0, 16, 2))
ax.set_xticks(np.arange(len(days)))
ax.set_xticklabels(days, rotation=45, ha='right')

# Annotate the peak usage
peak_day = 'Sunday'
peak_usage = total_usage[-1]
ax.annotate(f'Peak Usage: {peak_usage} hrs', xy=(6, peak_usage), xytext=(4.5, peak_usage + 1.5),
            arrowprops=dict(facecolor='darkred', arrowstyle='->'), fontsize=10, color='darkred')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()