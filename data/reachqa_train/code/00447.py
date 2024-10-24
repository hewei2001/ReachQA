import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator
import pandas as pd

# Generate weekly data for a year (2023)
weeks = pd.date_range(start="2023-01-01", periods=52, freq='W')

# Attendance data for each continent
africa_attendance = [120 + i * 2 + (i % 4) * 5 for i in range(52)]
asia_attendance = [220 + int(i * 2.5) + (i % 3) * 4 for i in range(52)]
europe_attendance = [180 + int(i * 1.8) + (i % 5) * 6 for i in range(52)]
north_america_attendance = [200 + i * 3 + (i % 6) * 3 for i in range(52)]
south_america_attendance = [150 + i * 2.2 + (i % 2) * 7 for i in range(52)]

# New data metric: Satisfaction score (0-100 scale)
africa_satisfaction = [60 + (i % 5) * 4 for i in range(52)]
asia_satisfaction = [70 - (i % 6) * 3 for i in range(52)]
europe_satisfaction = [75 + (i % 4) * 5 for i in range(52)]
north_america_satisfaction = [80 - (i % 3) * 2 for i in range(52)]
south_america_satisfaction = [65 + (i % 7) * 3 for i in range(52)]

# Initialize subplots
fig, ax1 = plt.subplots(figsize=(14, 10))
ax2 = ax1.twinx()  # Second y-axis for satisfaction scores

# Plot attendance data with different styles
ax1.plot(weeks, africa_attendance, marker='o', linestyle='-', color='green', linewidth=1.5, label='Africa')
ax1.plot(weeks, asia_attendance, marker='^', linestyle='--', color='red', linewidth=1.5, label='Asia')
ax1.plot(weeks, europe_attendance, marker='s', linestyle='-.', color='blue', linewidth=1.5, label='Europe')
ax1.plot(weeks, north_america_attendance, marker='D', linestyle=':', color='purple', linewidth=1.5, label='North America')
ax1.plot(weeks, south_america_attendance, marker='*', linestyle='-', color='orange', linewidth=1.5, label='South America')

# Plot satisfaction data
ax2.plot(weeks, africa_satisfaction, linestyle='-', color='darkgreen', alpha=0.5, linewidth=0.8)
ax2.plot(weeks, asia_satisfaction, linestyle='--', color='darkred', alpha=0.5, linewidth=0.8)
ax2.plot(weeks, europe_satisfaction, linestyle='-.', color='darkblue', alpha=0.5, linewidth=0.8)
ax2.plot(weeks, north_america_satisfaction, linestyle=':', color='darkviolet', alpha=0.5, linewidth=0.8)
ax2.plot(weeks, south_america_satisfaction, linestyle='-', color='darkorange', alpha=0.5, linewidth=0.8)

# Title and labels
ax1.set_title("Weekly Climate Change Awareness Event Attendance and Satisfaction\nAcross Continents in 2023", fontsize=16, fontweight='bold', wrap=True)
ax1.set_xlabel("Week", fontsize=12)
ax1.set_ylabel("Number of Attendees", fontsize=12)
ax2.set_ylabel("Satisfaction Score", fontsize=12, color='grey')

# Configure x-axis
ax1.xaxis.set_major_locator(MaxNLocator(nbins=13))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

# Add grid and legend
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()