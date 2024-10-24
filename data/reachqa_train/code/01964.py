import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.array([2020, 2022, 2024, 2026, 2028, 2030])

# Monthly active users (in millions) for different streaming categories
movies_streaming = np.array([5, 7, 8, 7, 6, 5])
tv_series_streaming = np.array([6, 9, 11, 12, 12, 11])
music_streaming = np.array([3, 4, 5, 7, 9, 11])
podcast_streaming = np.array([2, 3, 4, 5, 6, 7])

# Calculate total streaming users
total_streaming = movies_streaming + tv_series_streaming + music_streaming + podcast_streaming

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Fill areas between the lines and x-axis to create an area chart
ax.fill_between(years, 0, movies_streaming, label='Movies', color='#FF6347', alpha=0.7)
ax.fill_between(years, movies_streaming, movies_streaming + tv_series_streaming, label='TV Series', color='#4682B4', alpha=0.7)
ax.fill_between(years, movies_streaming + tv_series_streaming, movies_streaming + tv_series_streaming + music_streaming, label='Music', color='#32CD32', alpha=0.7)
ax.fill_between(years, movies_streaming + tv_series_streaming + music_streaming, total_streaming, label='Podcasts', color='#FFD700', alpha=0.7)

# Plot total streaming line
ax.plot(years, total_streaming, color='darkorchid', linewidth=2.5, linestyle='--', marker='o', label='Total Streaming Users')

# Annotate the plot with total numbers
for i, year in enumerate(years):
    ax.text(year, total_streaming[i] + 0.5, f'{total_streaming[i]}M', fontsize=10, ha='center', va='bottom', color='black', weight='bold')

# Set labels and title
ax.set_title('The Evolution of Streaming Service Usage\nin FutureCity from 2020 to 2030', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Monthly Active Users (Millions)', fontsize=14)

# Set x-ticks to improve readability
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=12, rotation=45)

# Grid, legend, and layout adjustments
ax.grid(visible=True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left', fontsize=12, frameon=False)

# Enhance visual aesthetics
ax.set_facecolor('#F7F7F9')
fig.patch.set_facecolor('#EDEDED')

# Adjust layout for no overlap
plt.tight_layout()

# Display the plot
plt.show()