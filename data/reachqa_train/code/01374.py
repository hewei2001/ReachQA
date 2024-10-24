import matplotlib.pyplot as plt
import numpy as np

# Academic departments
departments = ['Physics', 'Biology', 'Chemistry', 'Computer Science', 'Mathematics']

# Simulated research funding data (in thousands of dollars) for 2015-2025
funding_data = {
    'Physics': [500, 520, 480, 550, 570, 600, 620, 610, 640, 630, 650],
    'Biology': [300, 320, 310, 330, 340, 360, 380, 390, 400, 410, 420],
    'Chemistry': [400, 410, 415, 420, 430, 440, 450, 460, 470, 480, 490],
    'Computer Science': [600, 610, 620, 630, 640, 660, 670, 680, 690, 700, 710],
    'Mathematics': [200, 210, 205, 220, 225, 230, 240, 250, 255, 260, 270],
}

# Prepare the data for the box plot
funding_list = [funding_data[dept] for dept in departments]

# Compute average funding over the years for each department
avg_funding = [np.mean(funding_data[dept]) for dept in departments]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Boxplot configuration
box = ax.boxplot(funding_list, vert=True, patch_artist=True, labels=departments, notch=True)

# Customizing the appearance of the box plot
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
plt.setp(box['medians'], color='black')

# Adding a line plot for average funding
ax.plot(range(1, len(departments) + 1), avg_funding, color='purple', marker='o', linestyle='--', label='Average Funding')

# Titles and labels
ax.set_title('Yearly Distribution of Research Funding\nAcross Academic Departments (2015-2025)',
             fontsize=14, fontweight='bold', pad=20)
ax.set_ylabel('Funding (in $1000s)', fontsize=12)
ax.set_xlabel('Academic Department', fontsize=12)

# Customize grid and background
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_axisbelow(True)
ax.set_facecolor('#f9f9f9')

# Add a legend to distinguish box plot and line plot
ax.legend()

# Automatic layout adjustment
plt.tight_layout()

# Display the plot
plt.show()