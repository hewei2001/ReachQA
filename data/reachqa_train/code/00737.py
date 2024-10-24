import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2013, 2028)  # Extended to 2028 for a longer trend analysis

# Define more detailed streaming hours data for each genre (in millions)
popularity = {
    "Pop": [300, 320, 340, 360, 370, 380, 390, 410, 430, 450, 460, 470, 480, 485, 490],
    "Rock": [250, 240, 230, 220, 210, 200, 195, 190, 188, 185, 183, 182, 180, 179, 175],
    "Hip-Hop": [150, 170, 200, 230, 260, 290, 320, 350, 380, 410, 430, 440, 450, 460, 465],
    "Jazz": [60, 65, 60, 58, 55, 53, 50, 48, 47, 45, 44, 43, 42, 41, 40],
    "Electronic": [80, 85, 90, 95, 105, 110, 115, 120, 130, 135, 140, 142, 145, 148, 150],
    "Classical": [40, 42, 45, 48, 50, 52, 54, 56, 59, 60, 61, 63, 64, 65, 66],
    "Country": [30, 32, 34, 36, 38, 40, 42, 43, 45, 46, 47, 48, 49, 50, 51],
    "Reggae": [25, 27, 29, 30, 32, 31, 30, 28, 27, 26, 25, 24, 23, 22, 21]
}

# Introduce some variability in the data
variability = np.array([
    [0, 0, -5, 5, 0, -5, 0, 5, -10, 10, 0, -10, 5, 5, -5],
    [0, 5, -5, 0, 10, 0, 5, -5, 0, 5, -5, 0, 5, 0, -5],
    [5, 0, 10, 0, -10, 5, 0, 5, -5, 10, 0, 5, -10, 5, 0],
    [0, 5, 0, -5, 5, 0, -5, 0, 5, 0, -5, 0, -5, 0, 5],
    [5, 0, 5, 0, -5, 5, 0, -5, 0, 5, 0, -5, 5, 0, 0],
    [-5, 0, 5, 0, -5, 5, 0, -5, 0, 5, 0, 5, 0, -5, 5],
    [5, -5, 5, 0, -5, 0, 5, 0, -5, 0, 5, 0, -5, 0, 5],
    [0, 5, -5, 5, 0, -5, 5, 0, 5, -5, 0, 5, 0, -5, 5]
])

# Apply the variability to the data
data = np.array(list(popularity.values())) + variability

# Create the plot
fig, ax = plt.subplots(figsize=(14, 9))
colors = ['#FF9999', '#FFCC99', '#99CCFF', '#CCFF99', '#FFCCFF', '#FFFF99', '#B3B3CC', '#99FFCC']
ax.stackplot(years, data, labels=popularity.keys(), colors=colors)

# Set the title and axis labels
ax.set_title('Evolution of Music Genres in Streaming Platforms (2013-2028)', fontsize=16)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Streaming Hours (Millions)', fontsize=14)

# Create a legend and place it outside the plot
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

# Apply gridlines for better readability
ax.grid(alpha=0.3, linestyle='--')

# Add annotations for significant points
ax.annotate('Rise in Hip-Hop', xy=(2015, 200), xytext=(2015, 250),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=12, color='black')

ax.annotate('Steady Decline\nin Jazz', xy=(2020, 47), xytext=(2021, 70),
            arrowprops=dict(facecolor='blue', shrink=0.05),
            fontsize=12, color='blue')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()