import matplotlib.pyplot as plt
import numpy as np

# Define years for the data
years = np.arange(2015, 2024)

# Artificial data for podcast listeners (in millions)
podcast_data = {
    'True Crime': np.array([1, 3, 6, 9, 14, 16, 18, 20, 21]),
    'Technology': np.array([2, 4, 5, 7, 10, 14, 18, 23, 29]),
    'Health & Fitness': np.array([1, 2, 3, 5, 7, 9, 12, 15, 18]),
    'Comedy': np.array([3, 4, 6, 8, 10, 13, 15, 17, 20]),
}

# Extract values for stacking
values = np.array(list(podcast_data.values()))

# Calculate cumulative listeners each year
cumulative_listeners = values.sum(axis=0)

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the area chart with stacking
ax.stackplot(years, values, labels=podcast_data.keys(), colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'], alpha=0.8)

# Overlay line plot for cumulative listeners
ax.plot(years, cumulative_listeners, color='black', linewidth=2.5, linestyle='--', marker='o', label='Total Listeners')

# Set titles and labels
ax.set_title('Podcast Popularity Surge (2015-2023):\nRise of Genre-Specific and Overall Listening Trends', fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Listeners (millions)', fontsize=12)

# Annotate the total cumulative listeners at the end of 2023
ax.annotate(f'Total: {cumulative_listeners[-1]}M', xy=(2023, cumulative_listeners[-1]), xytext=(2020, cumulative_listeners[-1] + 10),
            arrowprops=dict(facecolor='gray', arrowstyle='->', lw=1.5),
            fontsize=11, fontweight='bold', color='black')

# Set legend in the upper left corner without a frame
ax.legend(loc='upper left', frameon=False)

# Enhance readability with grid lines
ax.grid(linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()