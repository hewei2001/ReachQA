import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Educational format popularity as percentages over the years
traditional_classroom = [70, 68, 65, 62, 60, 55, 52, 48, 45, 42, 40]
blended_learning = [20, 22, 23, 25, 27, 30, 32, 33, 35, 37, 38]
online_courses = [10, 10, 12, 13, 13, 15, 16, 19, 20, 21, 22]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the stacked area chart
ax.stackplot(years, traditional_classroom, blended_learning, online_courses,
             labels=['Traditional Classroom', 'Blended Learning', 'Online Courses'],
             colors=['#ff9999', '#66b3ff', '#99ff99'], alpha=0.8)

# Add titles and labels
ax.set_title('Trends in Educational Formats\nFrom Traditional to Online Learning (2010-2020)', fontsize=16, weight='bold')
ax.set_ylabel('Percentage of Implementation (%)', fontsize=12)
ax.set_xlabel('Year', fontsize=12)

# Add a legend outside the plot area
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Annotate significant shifts in trends
ax.axvline(2015, color='grey', linestyle='--', alpha=0.6)
ax.text(2016, 70, 'Blended Learning Initiatives\nGain Popularity', fontsize=9, color='black', rotation=90, va='center')

ax.axvline(2018, color='grey', linestyle='--', alpha=0.6)
ax.text(2019, 55, 'Rise of Online Course Platforms', fontsize=9, color='black', rotation=90, va='center')

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.5)

# Automatically adjust the layout for better viewing
plt.tight_layout(rect=[0, 0, 0.9, 1])

# Show the plot
plt.show()