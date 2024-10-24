import matplotlib.pyplot as plt
import numpy as np

# Data for years and museum attendance (in thousands)
years = np.arange(2010, 2021)
attendance = np.array([25, 28, 30, 32, 50, 55, 60, 63, 70, 85, 90])  # Attendance in thousands

# Calculate percentage increase in attendance year-over-year
attendance_growth = np.diff(attendance) / attendance[:-1] * 100
# Aligning the length of percentage growth with years
growth_years = years[1:]

# Create a plot for the line chart and bar chart
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the line chart with markers
ax1.plot(years, attendance, marker='o', color='royalblue', linewidth=2, label='Annual Attendance')
ax1.set_title('Annual Growth in Art Exhibit Attendance (2010-2020)\n with Year-over-Year Growth Percentage', fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Attendees (thousands)', fontsize=12, color='royalblue')
ax1.tick_params(axis='y', labelcolor='royalblue')
ax1.set_xlim(2010, 2020)
ax1.set_ylim(20, 100)

# Labeling each data point with its value
for i, j in zip(years, attendance):
    ax1.text(i, j + 2, f'{j}k', fontsize=9, ha='center', color='darkblue')

# Annotations for significant milestones
ax1.annotate('Major Exhibition Launch', xy=(2014, 50), xytext=(2012, 65),
            arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10, color='darkred')

ax1.annotate('Renowned Artist Collection', xy=(2019, 85), xytext=(2016, 75),
            arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=10, color='darkgreen')

# Second y-axis for percentage growth
ax2 = ax1.twinx()
ax2.bar(growth_years, attendance_growth, color='orange', alpha=0.5, width=0.5, label='Year-over-Year Growth (%)')
ax2.set_ylabel('Year-over-Year Growth (%)', fontsize=12, color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
ax2.set_ylim(0, 100)

# Legend for both plots
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=10)

# Grid to enhance readability
ax1.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()