import matplotlib.pyplot as plt
import numpy as np

# Years for the dataset
years = np.arange(2010, 2021)

# Enrollment data for each discipline in social sciences and humanities
enrollments = {
    "Anthropology": [300, 320, 340, 360, 380, 400, 450, 470, 480, 490, 500],
    "Sociology": [280, 290, 310, 330, 350, 370, 390, 420, 450, 460, 470],
    "History": [260, 270, 280, 300, 320, 340, 360, 370, 380, 400, 410],
    "Philosophy": [240, 250, 260, 280, 300, 320, 330, 340, 350, 360, 370],
    "Literature": [220, 230, 240, 250, 270, 290, 310, 320, 330, 340, 350],
}

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Set x positions for grouped bar chart
x = np.arange(len(years))
bar_width = 0.15

# Color palette for different disciplines
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Plotting each discipline's data as bars
for i, (discipline, counts) in enumerate(enrollments.items()):
    ax.bar(x + i * bar_width, counts, width=bar_width, label=discipline, color=colors[i], edgecolor='grey')
    for j, count in enumerate(counts):
        ax.text(x[j] + i * bar_width, count + 5, f'{count}', ha='center', va='bottom', fontsize=9)

# Set title and labels
ax.set_title("Rising Engagement in Social Sciences and Humanities:\nStudent Enrollments from 2010 to 2020",
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of Enrollments", fontsize=12)
ax.set_xticks(x + 2 * bar_width)
ax.set_xticklabels(years, fontsize=10, rotation=45)

# Add legend to differentiate disciplines
ax.legend(title="Disciplines", loc='upper left', bbox_to_anchor=(1, 1))

# Add gridlines along the y-axis for better readability
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Automatically adjust layout to prevent overlaps
plt.tight_layout()

# Display the plot
plt.show()