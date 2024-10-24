import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Dolphin populations in thousands for each oceanic region
pacific_population = np.array([120, 125, 130, 135, 140, 138, 137, 142, 145, 147, 150])
atlantic_population = np.array([110, 113, 115, 118, 120, 123, 127, 130, 133, 137, 140])
indian_population = np.array([90, 92, 94, 97, 100, 105, 108, 112, 115, 117, 119])

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the dolphin populations for each oceanic region
ax.plot(years, pacific_population, marker='o', linestyle='-', color='dodgerblue', linewidth=2, label='Pacific Ocean')
ax.plot(years, atlantic_population, marker='s', linestyle='--', color='forestgreen', linewidth=2, label='Atlantic Ocean')
ax.plot(years, indian_population, marker='^', linestyle='-.', color='orangered', linewidth=2, label='Indian Ocean')

# Set the title and labels with line breaks for readability
ax.set_title('Ocean Conservation Efforts:\nTracking Dolphin Populations Over Time', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Dolphin Population (Thousands)', fontsize=12, fontweight='bold')

# Enable grid lines
ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Add a legend
ax.legend(loc='upper left', fontsize=10, frameon=False)

# Highlight the significant conservation success in the Pacific Ocean from 2015 to 2017
ax.axvspan(2015, 2017, color='lightblue', alpha=0.3, label='Pacific Success Initiative')

# Annotate the chart to highlight notable trends or successes
ax.annotate('Pacific Success', xy=(2016, 138), xytext=(2014, 145),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue'),
            fontsize=10, color='blue')

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()