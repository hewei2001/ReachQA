import matplotlib.pyplot as plt
import numpy as np

# Define the genres
categories = ['Action', 'Adventure', 'Strategy', 'Role-Playing', 'Simulation']
# Number of variables we're plotting
num_vars = len(categories)

# Average player ratings on a scale from 1 to 10 for each genre
ratings = [8.5, 7.8, 8.0, 8.3, 7.5]

# Compute the angle for each category on the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot should form a complete circle, hence we need to repeat the first value at the end
ratings += ratings[:1]
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

# Draw one of the filled areas
ax.fill(angles, ratings, color='skyblue', alpha=0.4)
ax.plot(angles, ratings, color='blue', linewidth=2)

# Customize the appearance of the chart
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, color='darkblue')

# Set the title with multiline adjustment
plt.title('Gaming Preferences in 2023:\nA Radar Chart Exploration', 
          size=16, color='darkblue', y=1.1, va='center', ha='center')

# Add a legend
ax.legend(['Average Ratings'], loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=10)

# Ensure layout adjustments to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()