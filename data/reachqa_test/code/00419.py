import matplotlib.pyplot as plt
import numpy as np

# Data for the number of innovations from each country in different categories
countries = ['USA', 'China', 'Germany', 'Japan', 'UK', 'South Korea', 'France', 'Russia', 'India', 'Israel']
tech_innovations = [300, 250, 190, 180, 150, 120, 100, 75, 65, 55]
healthcare_innovations = [200, 220, 130, 100, 80, 70, 60, 50, 45, 35]
enviro_innovations = [150, 180, 120, 120, 90, 60, 45, 35, 30, 25]

# Creating a horizontal grouped bar chart
width = 0.25  # Width of the bars

fig, ax = plt.subplots(figsize=(12, 10))

# Position of the bars on the y-axis
ind = np.arange(len(countries))

# Create the bars
tech_bars = ax.barh(ind, tech_innovations, width, label='Technology', color='lightcoral')
healthcare_bars = ax.barh(ind + width, healthcare_innovations, width, label='Healthcare', color='lightskyblue')
enviro_bars = ax.barh(ind + 2 * width, enviro_innovations, width, label='Environment', color='lightgreen')

# Add labels to the bars showing the number of innovations
for bar_group in [tech_bars, healthcare_bars, enviro_bars]:
    for bar in bar_group:
        xval = bar.get_width()
        yval = bar.get_y() + bar.get_height() / 2
        ax.text(xval + 5, yval, s=int(xval), va='center', ha='left', fontsize=9)

# Set the y-axis labels and ticks
ax.set_yticks(ind + 1.5 * width)
ax.set_yticklabels(countries)

# Adding labels, title, and legend
ax.set_xlabel('Number of Innovations')
ax.set_title("Global Innovations by Country\n(1923-2023)\nCategorized by Field", fontsize=12, loc='left', wrap=True)
ax.legend(title="Field", loc='upper right')

# Adjusting layout
plt.tight_layout()

# Show the chart
plt.show()