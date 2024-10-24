import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Subscription trends (in percentage) for each genre over the years
drama = np.array([25, 24, 23, 22, 23, 24, 25, 26, 27, 28, 29])
comedy = np.array([20, 21, 22, 22, 21, 21, 20, 19, 18, 17, 16])
documentary = np.array([10, 11, 12, 13, 14, 15, 15, 16, 16, 17, 17])
action = np.array([25, 25, 25, 25, 25, 24, 23, 22, 21, 20, 19])
sci_fi = np.array([20, 19, 18, 18, 17, 16, 17, 17, 18, 18, 19])

# Stacking the data for the area plot
data = np.vstack([drama, comedy, documentary, action, sci_fi])

# Define colors for each genre
colors = ['#FF6347', '#FFD700', '#32CD32', '#87CEEB', '#8A2BE2']

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, data, labels=['Drama', 'Comedy', 'Documentary', 'Action', 'Science Fiction'], colors=colors, alpha=0.8)

# Customizing the plot
ax.set_title("Streaming Service Subscription Trends\nAcross Genres (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Subscription Distribution (%)", fontsize=12)
ax.set_xlim(2010, 2020)
ax.set_ylim(0, 100)

# Add a grid for better readability
ax.grid(True, which='both', linestyle='--', alpha=0.7)

# Rotating the x-axis labels for clarity
plt.xticks(years, rotation=45)

# Adding a legend
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1), title="Genres")

# Use tight layout to prevent clipping of labels
plt.tight_layout()

# Display the plot
plt.show()