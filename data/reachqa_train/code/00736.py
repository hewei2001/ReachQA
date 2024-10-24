import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2013, 2024)

# Define the streaming hours data for each genre (in millions)
popularity = {
    "Pop": [300, 320, 340, 360, 370, 380, 390, 410, 430, 450, 460],
    "Rock": [250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 155],
    "Hip-Hop": [150, 170, 200, 230, 260, 290, 320, 350, 380, 410, 430],
    "Jazz": [60, 65, 60, 58, 55, 53, 50, 48, 47, 45, 43],
    "Electronic": [80, 85, 90, 95, 105, 110, 115, 120, 130, 135, 140],
    "Classical": [40, 42, 45, 48, 50, 52, 54, 56, 59, 60, 61]
}

# Stack data into a numpy array for plotting
data = np.array(list(popularity.values()))

# Plotting the stacked area chart
plt.figure(figsize=(14, 8))
colors = ['#FF9999', '#FFCC99', '#99CCFF', '#CCFF99', '#FFCCFF', '#FFFF99']
plt.stackplot(years, data, labels=popularity.keys(), colors=colors)

# Set title and axis labels
plt.title('The Evolution of Music Genres\nin Streaming Platforms (2013-2023)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Streaming Hours (in Millions)', fontsize=14)

# Create legend and position it outside the plot
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

# Apply gridlines for better readability
plt.grid(alpha=0.3, linestyle='--')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()