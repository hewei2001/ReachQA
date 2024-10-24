import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
green_spaces = {
    "New York": np.array([200, 220, 260, 300, 350, 400]),
    "London": np.array([150, 170, 190, 210, 230, 260]),
    "Tokyo": np.array([180, 200, 210, 240, 280, 310]),
    "Sydney": np.array([130, 160, 190, 220, 260, 300]),
    "Paris": np.array([110, 140, 160, 180, 210, 250])
}

# Colors for each city's area
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create an area chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each city's green space development
for (city, data), color in zip(green_spaces.items(), colors):
    ax.fill_between(years, data, label=city, color=color, alpha=0.7)

# Customizing the plot
ax.set_title("Growth of Urban Green Spaces Over a Decade:\nA Comparison of Major Cities", fontsize=14, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Green Space (Hectares)", fontsize=12)
ax.set_xticks(years)
ax.legend(title='Cities', fontsize=10, loc='upper left')

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Adjusting x-axis labels for better readability
plt.xticks(years, rotation=45)

# Automatically adjust subplot params to give specified padding.
plt.tight_layout()

# Display the plot
plt.show()