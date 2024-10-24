import matplotlib.pyplot as plt
import numpy as np

# Decades from 1950 to 2020
decades = np.array(['1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s'])

# Popularity scores for each genre across the decades
jazz_popularity = [70, 60, 50, 45, 40, 35, 30, 25]
rock_popularity = [30, 60, 80, 85, 75, 70, 60, 50]
classical_popularity = [80, 70, 65, 60, 55, 50, 45, 40]
blues_popularity = [50, 45, 40, 35, 30, 25, 20, 15]

# Total music consumption score
total_music_consumption = [230, 235, 235, 225, 200, 180, 155, 130]

# Prepare data for stacking
popularity_data = np.vstack([jazz_popularity, rock_popularity, classical_popularity, blues_popularity])
cumulative_data = np.cumsum(popularity_data, axis=0)

# Colors for each genre
colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF6347']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 9))

# Plot the stacked area chart
ax.fill_between(decades, 0, cumulative_data[0], color=colors[0], label='Jazz', alpha=0.8)
ax.fill_between(decades, cumulative_data[0], cumulative_data[1], color=colors[1], label='Rock \'n\' Roll', alpha=0.8)
ax.fill_between(decades, cumulative_data[1], cumulative_data[2], color=colors[2], label='Classical', alpha=0.8)
ax.fill_between(decades, cumulative_data[2], cumulative_data[3], color=colors[3], label='Blues', alpha=0.8)

# Overlay a line plot showing total music consumption
ax.plot(decades, total_music_consumption, color='purple', linestyle='--', linewidth=2, marker='o', label='Total Music Consumption')

# Set titles and labels
ax.set_title("The Rise of Vintage Music Genres\nOver the Decades (1950-2020) with Total Music Consumption", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decades', fontsize=14)
ax.set_ylabel('Popularity Score / Consumption', fontsize=14)

# Customize x-axis
ax.set_xticks(np.arange(len(decades)))
ax.set_xticklabels(decades, fontsize=12, rotation=45, ha='right')

# Add a legend
ax.legend(loc='upper left', fontsize=12, ncol=1)

# Add grid lines for readability
ax.grid(True, which='both', axis='y', linestyle='--', alpha=0.6)

# Auto-adjust layout
plt.tight_layout()

# Show the plot
plt.show()