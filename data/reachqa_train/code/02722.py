import matplotlib.pyplot as plt
import numpy as np

# Defining the study hours data for each discipline
engineering_hours = [20, 22, 19, 24, 18, 21, 23, 20, 22, 19, 24, 18, 21, 20, 23, 25, 19, 22, 24, 21]
arts_hours = [15, 17, 14, 16, 18, 13, 17, 16, 15, 14, 16, 19, 15, 17, 18, 14, 16, 17, 13, 19]
sciences_hours = [25, 27, 26, 23, 28, 24, 25, 27, 26, 23, 24, 28, 24, 25, 27, 26, 28, 23, 24, 25]
business_hours = [18, 20, 19, 21, 22, 17, 20, 21, 19, 22, 18, 20, 21, 23, 17, 19, 22, 21, 20, 18]
humanities_hours = [16, 18, 17, 15, 19, 14, 18, 17, 15, 16, 19, 18, 14, 15, 17, 16, 19, 18, 14, 15]

# Combine the data into a list for the boxplot
data = [engineering_hours, arts_hours, sciences_hours, business_hours, humanities_hours]

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Create the boxplot
box = ax.boxplot(data, patch_artist=True, labels=['Engineering', 'Arts', 'Sciences', 'Business', 'Humanities'], notch=True, vert=True)

# Customizing boxplot colors for each discipline
colors = ['#E63946', '#F1A208', '#4A4E69', '#9A8C98', '#C9ADA7']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Styling elements
for whisker in box['whiskers']:
    whisker.set(color='gray', linewidth=1.5, linestyle='--')
for cap in box['caps']:
    cap.set(color='gray', linewidth=1.5)
for median in box['medians']:
    median.set(color='black', linewidth=2)

# Setting labels and title
ax.set_xlabel('Disciplines', fontsize=12)
ax.set_ylabel('Study Hours per Week', fontsize=12)
ax.set_title('Study Hour Distribution Across University Disciplines:\nA Box Plot Analysis', fontsize=14, fontweight='bold', pad=20)

# Display grid
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()