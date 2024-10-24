import matplotlib.pyplot as plt
import numpy as np

# Define years for the data
years = np.arange(2010, 2021)

# Manually crafted data for EV registrations (in thousands)
north_america_ev = [20, 25, 30, 50, 75, 110, 160, 230, 320, 450, 600]
europe_ev = [15, 18, 25, 35, 50, 80, 130, 200, 300, 430, 580]
asia_ev = [10, 15, 20, 35, 60, 100, 150, 250, 400, 600, 850]

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the line chart for each region
ax.plot(years, north_america_ev, marker='o', linestyle='-', color='blue', linewidth=2, label='North America')
ax.plot(years, europe_ev, marker='s', linestyle='-', color='green', linewidth=2, label='Europe')
ax.plot(years, asia_ev, marker='^', linestyle='-', color='red', linewidth=2, label='Asia')

# Setting title and labels
ax.set_title('Electric Vehicle Registrations by Region\n(2010-2020)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Registrations (in thousands)', fontsize=12)

# Adding a legend to identify regions
ax.legend(loc='upper left', fontsize=10, title='Regions', title_fontsize=12)

# Enable grid for easier value estimation
ax.grid(True, linestyle='--', alpha=0.7)

# Ensuring x-tick labels are readable by rotating them
plt.xticks(years, rotation=45)

# Annotating key points in the data
ax.annotate('Rapid growth in Asia', xy=(2019, 600), xytext=(2015, 700),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='darkred')
ax.annotate('Initial surge in North America', xy=(2013, 50), xytext=(2011, 150),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='darkblue')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()