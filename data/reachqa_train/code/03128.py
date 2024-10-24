import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Streams (in millions) for each genre over the years
pop_streams = np.array([120, 130, 150, 170, 180, 190, 210, 230, 250, 270, 300])
rock_streams = np.array([100, 105, 110, 115, 120, 130, 135, 140, 145, 150, 160])
hiphop_streams = np.array([80, 85, 95, 110, 120, 140, 160, 180, 200, 220, 250])
classical_streams = np.array([40, 42, 45, 48, 50, 52, 55, 60, 65, 70, 75])
electronic_streams = np.array([60, 70, 80, 85, 90, 100, 110, 120, 130, 140, 150])

# Stack the data for the area plot
streams_data = np.vstack([pop_streams, rock_streams, hiphop_streams, classical_streams, electronic_streams])

# Define genre labels and colors
genres = ['Pop', 'Rock', 'Hip Hop', 'Classical', 'Electronic']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, streams_data, labels=genres, colors=colors, alpha=0.85)

# Add chart details
ax.set_title("Decade of Streaming: \nMusic Genre Popularity Trends (2010-2020)", fontsize=14, fontweight='bold', loc='left')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Millions of Streams', fontsize=12)
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='medium')

# Customize x and y ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 901, 100))
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Improve layout to avoid overlapping elements
plt.tight_layout()

# Show the plot
plt.show()