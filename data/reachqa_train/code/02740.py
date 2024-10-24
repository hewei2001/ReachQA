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

# Calculate total and cumulative preferences for a different perspective
total_data = action_data + drama_data + comedy_data + scifi_data
cumulative_action = np.cumsum(action_data)
cumulative_drama = np.cumsum(drama_data)
cumulative_comedy = np.cumsum(comedy_data)
cumulative_scifi = np.cumsum(scifi_data)

# Initialize the figure and two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

# Plot stacked bars in the first subplot
ax1.bar(years, action_data, label='Action', color='#FF5733', alpha=0.8)
ax1.bar(years, drama_data, bottom=action_data, label='Drama', color='#33FF57', alpha=0.8)
ax1.bar(years, comedy_data, bottom=action_data + drama_data, label='Comedy', color='#3357FF', alpha=0.8)
ax1.bar(years, scifi_data, bottom=action_data + drama_data + comedy_data, label='Sci-Fi', color='#FFC300', alpha=0.8)

# Set titles and labels for the first subplot
ax1.set_title('Movie Genre Preferences:\nA Five-Year Perspective (2016-2020)', fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Preference (%)', fontsize=12)
ax1.legend(title='Genres', loc='upper right', fontsize=10)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.set_ylim(0, 100)

# Plot a line chart in the second subplot
ax2.plot(years, cumulative_action, marker='o', label='Cumulative Action', color='#FF5733')
ax2.plot(years, cumulative_drama, marker='s', label='Cumulative Drama', color='#33FF57')
ax2.plot(years, cumulative_comedy, marker='^', label='Cumulative Comedy', color='#3357FF')
ax2.plot(years, cumulative_scifi, marker='d', label='Cumulative Sci-Fi', color='#FFC300')

# Set titles and labels for the second subplot
ax2.set_title('Cumulative Genre Preferences Over Years', fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Cumulative Preference', fontsize=12)
ax2.legend(title='Cumulative Genres', loc='upper left', fontsize=10)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display plot
plt.show()