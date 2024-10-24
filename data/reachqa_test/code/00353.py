import matplotlib.pyplot as plt
import numpy as np

# Data
companies = ['Coursera', 'Udemy', 'edX', 'Khan Academy', 'Pluralsight', 'Chegg', 'VIPKid', 'Byju\'s', 'Duolingo', 'McGraw-Hill Education', 'FutureLearn', 'Codecademy', 'DataCamp', 'Platinum Educational Group', 'Scholastic Learn at Home']

revenue_2015 = [100, 80, 60, 50, 40, 30, 25, 20, 15, 10, 90, 70, 65, 60, 55]
revenue_2016 = [120, 95, 70, 60, 50, 40, 35, 30, 25, 20, 110, 90, 85, 80, 75]
revenue_2017 = [150, 110, 85, 75, 65, 55, 50, 45, 40, 35, 130, 115, 110, 105, 100]
revenue_2018 = [180, 130, 100, 90, 80, 70, 65, 60, 55, 50, 150, 140, 135, 130, 125]
revenue_2019 = [220, 160, 120, 110, 100, 90, 85, 80, 75, 70, 170, 165, 160, 155, 150]
revenue_2020 = [280, 200, 150, 140, 130, 120, 115, 110, 105, 100, 200, 195, 190, 185, 180]
revenue_2021 = [350, 250, 180, 170, 160, 150, 145, 140, 135, 130, 230, 225, 220, 215, 210]
revenue_2022 = [420, 300, 220, 210, 200, 190, 185, 180, 175, 170, 260, 255, 250, 245, 240]

years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
data = [revenue_2015, revenue_2016, revenue_2017, revenue_2018, revenue_2019, revenue_2020, revenue_2021, revenue_2022]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Plot bar chart
bar_width = 0.08
for i, year_data in enumerate(data):
    ax.bar(np.arange(len(companies)) + i*bar_width, year_data, width=bar_width, label=years[i], color=plt.cm.tab20(i))

# Add text labels above bars
for i, year_data in enumerate(data):
    for j, value in enumerate(year_data):
        ax.text(j + i*bar_width, value + 2, str(value), ha='center', va='bottom', fontsize=10, rotation=45)

# Set title and labels
ax.set_title("The Evolution of Educational Technology:\nTop 15 EdTech Companies by Revenue (2015-2022)")
ax.set_xlabel("Companies")
ax.set_ylabel("Revenue (Millions)")

# Set x-axis tick labels
ax.set_xticks(np.arange(len(companies)))
ax.set_xticklabels(companies, rotation=45, ha='right')

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.05, 1), ncol=1)

# Add grid lines
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Adjust layout
fig.tight_layout(rect=[0, 0, 1, 0.92])

# Show the plot
plt.show()