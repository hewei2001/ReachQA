import matplotlib.pyplot as plt
import numpy as np

# Data
practice_areas = ['Criminal Law', 'Family Law', 'Corporate Law', 'Intellectual Property Law', 'Tax Law', 'Bankruptcy Law', 'Immigration Law', 'Environmental Law']
num_lawyers = [15000, 12000, 10000, 8000, 7000, 6000, 5000, 4000]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Set bar positions
bar_positions = np.arange(len(practice_areas))

# Plot bar chart
ax.bar(bar_positions, num_lawyers, color='#87CEEB', width=0.7, edgecolor='black')

# Add text labels above the bars
for i, num_lawyer in enumerate(num_lawyers):
    ax.text(i, num_lawyer + 500, f"{num_lawyer}", ha='center', va='bottom', fontsize=10, weight='bold')

# Set title and labels
ax.set_title("Distribution of Lawyers in the United States\nby Practice Area", fontsize=14, weight='bold')
ax.set_xlabel("Practice Area", fontsize=12)
ax.set_ylabel("Number of Lawyers", fontsize=12)

# Set x-axis tick labels
ax.set_xticks(bar_positions)
ax.set_xticklabels(practice_areas, rotation=45, ha='right', fontsize=10)

# Add grid
ax.grid(True, axis='y', linestyle='--', alpha=0.5)

# Add a horizontal line at the average number of lawyers
avg_lawyers = np.mean(num_lawyers)
ax.axhline(avg_lawyers, color='gray', linestyle='--', label=f'Average: {avg_lawyers:.0f}')

# Add a legend
ax.legend(loc='upper right')

# Automatically adjust the image layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show plot
plt.show()