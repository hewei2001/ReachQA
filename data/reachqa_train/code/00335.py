import matplotlib.pyplot as plt
import numpy as np

# Defining the months of the year
months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

# Average practice hours per month for a group of young violin students
practice_hours = [10, 12, 15, 18, 20, 17, 14, 13, 15, 18, 20, 22]

# Create the plot
plt.figure(figsize=(12, 6), dpi=100)

# Plot the data as a line chart
plt.plot(months, practice_hours, color='teal', marker='o', linestyle='-', linewidth=2, markersize=8, label='Avg. Practice Hours')

# Title and labels
plt.title("The Golden Strings:\nMonthly Violin Practice Trends Among Young Musicians in 2023", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Average Practice Hours", fontsize=12)

# Enhancing the plot with a grid and legend
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.yticks(np.arange(0, 25, 2))
plt.legend(loc='upper left', fontsize=10)
plt.tight_layout()

# Add annotations for key insights
plt.annotate(
    'Recital Preparation Peak', 
    xy=('May', 20), xytext=('March', 22),
    arrowprops=dict(facecolor='grey', shrink=0.05, width=1, headwidth=8),
    fontsize=10, fontweight='bold', color='darkred'
)

plt.annotate(
    'Summer Vacation Lull', 
    xy=('July', 14), xytext=('June', 16),
    arrowprops=dict(facecolor='grey', shrink=0.05, width=1, headwidth=8),
    fontsize=10, fontweight='bold', color='darkblue'
)

plt.annotate(
    'End-of-Year Focus', 
    xy=('December', 22), xytext=('October', 23),
    arrowprops=dict(facecolor='grey', shrink=0.05, width=1, headwidth=8),
    fontsize=10, fontweight='bold', color='green'
)

# Display the plot
plt.show()