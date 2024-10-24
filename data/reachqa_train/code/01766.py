import matplotlib.pyplot as plt
import numpy as np

# Original data for the box plot
community_engagement = [78, 82, 69, 85, 71]
access_to_amenities = [90, 87, 76, 88, 75]
environmental_quality = [65, 70, 60, 78, 65]
safety = [80, 85, 75, 82, 70]
data = [community_engagement, access_to_amenities, environmental_quality, safety]
categories = ['Community Engagement', 'Access to Amenities', 'Environmental Quality', 'Safety']

# New data for the line plot (average scores over time)
years = np.array([2018, 2019, 2020, 2021, 2022])
avg_community_engagement = np.array([70, 73, 75, 78, 80])
avg_access_to_amenities = np.array([85, 87, 88, 89, 90])
avg_environmental_quality = np.array([60, 62, 65, 67, 70])
avg_safety = np.array([72, 74, 76, 78, 80])

# Set up the plotting area with 1 row and 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Box Plot
box_colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow']
box = ax1.boxplot(data, vert=False, patch_artist=True,
                  boxprops=dict(color='blue'), whiskerprops=dict(color='blue'),
                  capprops=dict(color='blue'), flierprops=dict(markerfacecolor='red', marker='o', color='blue'),
                  medianprops=dict(color='darkblue'))

for patch, color in zip(box['boxes'], box_colors):
    patch.set_facecolor(color)

ax1.set_yticklabels(categories)
ax1.set_title("Community Well-Being Distribution\nin Urban Neighborhoods", fontsize=14, fontweight='bold')
ax1.set_xlabel('Scores', fontsize=12)
ax1.set_ylabel('Categories', fontsize=12)
ax1.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Line Plot
ax2.plot(years, avg_community_engagement, label='Community Engagement', color='lightblue', marker='o', linestyle='-')
ax2.plot(years, avg_access_to_amenities, label='Access to Amenities', color='lightgreen', marker='s', linestyle='--')
ax2.plot(years, avg_environmental_quality, label='Environmental Quality', color='lightcoral', marker='^', linestyle='-.')
ax2.plot(years, avg_safety, label='Safety', color='lightyellow', marker='d', linestyle=':')

ax2.set_title("Average Community Well-Being Scores Over Time", fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Average Scores', fontsize=12)
ax2.legend(loc='upper left', fontsize=10)
ax2.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
ax2.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the combined plot
plt.show()