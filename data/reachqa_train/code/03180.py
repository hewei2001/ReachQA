import matplotlib.pyplot as plt
import numpy as np

# Data for years and museum attendance (in thousands)
years = np.arange(2010, 2021)
attendance = np.array([25, 28, 30, 32, 50, 55, 60, 63, 70, 85, 90])  # Attendance in thousands

# Create a plot for the line chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the line chart with markers
ax.plot(years, attendance, marker='o', color='royalblue', linewidth=2, linestyle='-', label='Annual Attendance')

# Annotations for significant milestones
ax.annotate('Major Exhibition Launch', xy=(2014, 50), xytext=(2012, 60),
            arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10, color='darkred')

ax.annotate('Renowned Artist Collection', xy=(2019, 85), xytext=(2016, 75),
            arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=10, color='darkgreen')

# Titles and labels
ax.set_title('Annual Growth in Art Exhibit Attendance\n(2010-2020)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Attendees (thousands)', fontsize=12)

# Grid to enhance readability
ax.grid(True, linestyle='--', alpha=0.6)

# Setting limits for axes
ax.set_xlim(2010, 2020)
ax.set_ylim(20, 100)

# Labeling each data point with its value
for i, j in zip(years, attendance):
    ax.text(i, j + 2, f'{j}k', fontsize=9, ha='center', color='darkblue')

# Legend for the chart
ax.legend(loc='upper left', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()