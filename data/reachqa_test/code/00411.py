import matplotlib.pyplot as plt
import numpy as np

# Constructing contextual data for Space Exploration Missions Duration Analysis
decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
# Fabricated data for mission durations and variations
average_durations = [30, 15, 120, 180, 150, 250, 300]  # in days
duration_variations = [5, 3, 10, 15, 20, 25, 30]  # error bar, uncertainty or variation in duration

# Fabricated data for number of missions per decade
missions_per_decade = [5, 8, 12, 20, 30, 45, 60]  # Number of space missions

# Creating the figure and a grid of subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

# Plotting the line chart in the top subplot
line, = ax1.plot(decades, average_durations, marker='o', linestyle='-', color='blue', label='Average Duration')
ax1.errorbar(decades, average_durations, yerr=duration_variations, fmt='none', ecolor='red', capsize=5, alpha=0.5)

# Setting labels and title for the top subplot
ax1.set_ylabel('Mission Duration (Days)')
ax1.set_title('Decade-wise\nDuration Trends\nof Space Missions')
ax1.legend([line], ['Average Mission Duration'], loc='upper left')

# Plotting the bar chart in the bottom subplot
ax2.bar(decades, missions_per_decade, color='green', edgecolor='black')

# Setting labels and title for the bottom subplot
ax2.set_xlabel('Decades')
ax2.set_ylabel('Number of Missions')
ax2.set_title('Missions per Decade')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(hspace=0.5)

# Automatically adjust the image layout
plt.tight_layout()

# Show plot
plt.show()