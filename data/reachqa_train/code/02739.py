import matplotlib.pyplot as plt
import numpy as np

# Define the years and genres
years = np.array([2016, 2017, 2018, 2019, 2020])
genres = ['Action', 'Drama', 'Comedy', 'Sci-Fi']

# Define the data for each genre (in percentages)
action_data = np.array([30, 32, 35, 31, 33])
drama_data = np.array([20, 18, 17, 21, 22])
comedy_data = np.array([25, 26, 25, 24, 20])
scifi_data = np.array([25, 24, 23, 24, 25])

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting stacked bars
ax.bar(years, action_data, label='Action', color='#FF5733', alpha=0.8)
ax.bar(years, drama_data, bottom=action_data, label='Drama', color='#33FF57', alpha=0.8)
ax.bar(years, comedy_data, bottom=action_data + drama_data, label='Comedy', color='#3357FF', alpha=0.8)
ax.bar(years, scifi_data, bottom=action_data + drama_data + comedy_data, label='Sci-Fi', color='#FFC300', alpha=0.8)

# Set titles and labels
ax.set_title('Movie Genre Preferences:\nA Five-Year Perspective (2016-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Preference (%)', fontsize=13)

# Add legend
ax.legend(title='Genres', loc='upper right', fontsize=11)

# Add grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Set y-axis limits
ax.set_ylim(0, 100)

# Adjust layout
plt.tight_layout()

# Display plot
plt.show()