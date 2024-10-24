import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.arange(2013, 2024)

# Define the attendance in thousands for each genre over the years
attendance_pop = [20, 25, 30, 40, 55, 70, 100, 130, 160, 180, 210]
attendance_rock = [15, 20, 25, 30, 45, 60, 80, 100, 120, 140, 170]
attendance_classical = [5, 6, 7, 10, 15, 20, 25, 30, 35, 45, 50]
attendance_electronic = [10, 15, 20, 35, 50, 65, 90, 110, 130, 160, 200]

# Define the hypothetical revenue in millions for each genre over the years
revenue_pop = [5, 7, 10, 14, 20, 25, 30, 40, 50, 55, 70]
revenue_rock = [4, 5, 7, 9, 14, 18, 24, 30, 35, 40, 55]
revenue_classical = [1, 1.5, 2, 3, 5, 6, 8, 10, 12, 15, 18]
revenue_electronic = [2, 3, 5, 9, 12, 15, 22, 28, 34, 45, 60]

# Create the main plot with line plots for attendance
fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, attendance_pop, marker='o', label='Pop Attendance', color='crimson', linewidth=2)
ax1.plot(years, attendance_rock, marker='s', label='Rock Attendance', color='royalblue', linewidth=2)
ax1.plot(years, attendance_classical, marker='d', label='Classical Attendance', color='green', linewidth=2)
ax1.plot(years, attendance_electronic, marker='^', label='Electronic Attendance', color='orange', linewidth=2)

# Add titles and labels for the primary axis
ax1.set_title('Virtual Concert Attendance Trends and Revenue Insights (2013-2023)', fontsize=16, weight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Attendees (Thousands)', fontsize=12)

# Create a secondary y-axis for the overlay bar plot
ax2 = ax1.twinx()
bar_width = 0.2
ax2.bar(years - bar_width*1.5, revenue_pop, width=bar_width, label='Pop Revenue', color='crimson', alpha=0.3)
ax2.bar(years - bar_width/2, revenue_rock, width=bar_width, label='Rock Revenue', color='royalblue', alpha=0.3)
ax2.bar(years + bar_width/2, revenue_classical, width=bar_width, label='Classical Revenue', color='green', alpha=0.3)
ax2.bar(years + bar_width*1.5, revenue_electronic, width=bar_width, label='Electronic Revenue', color='orange', alpha=0.3)

# Secondary y-axis label
ax2.set_ylabel('Revenue (Millions)', fontsize=12)

# Add a legend
ax1.legend(loc='upper left', fontsize=10, frameon=True)
ax2.legend(loc='upper right', fontsize=10, frameon=True)

# Annotate significant milestones
ax1.annotate('Major Tech Shift', xy=(2017, 75), xytext=(2014, 150),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='black')

ax1.annotate('Global Event Impact', xy=(2020, 175), xytext=(2018, 210),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='black')

# Customize grid and ticks
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.set_yticks(np.arange(0, 251, 50))
ax2.set_yticks(np.arange(0, 81, 20))

# Automatically adjust the plot layout
fig.tight_layout()

# Display the plot
plt.show()