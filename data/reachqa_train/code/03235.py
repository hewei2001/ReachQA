import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2013, 2024)

# Define the usage index for each communication platform over the years
traditional_mail = np.array([80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30])
email = np.array([60, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71])
social_media = np.array([10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100])
instant_messaging = np.array([15, 18, 25, 35, 50, 65, 80, 95, 110, 125, 140])
video_conferencing = np.array([5, 5, 6, 7, 8, 12, 20, 35, 50, 75, 100])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Create the stacked area chart
ax.stackplot(years, traditional_mail, email, social_media, instant_messaging, video_conferencing,
             labels=['Traditional Mail', 'Email', 'Social Media', 'Instant Messaging', 'Video Conferencing'],
             colors=['#d4e157', '#81c784', '#64b5f6', '#9575cd', '#f06292'], alpha=0.85)

# Set title and labels with font enhancements
ax.set_title('Evolution of Communication Platforms\nin Communicastan (2013-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Platform Usage Index (arbitrary units)', fontsize=12)

# Add a legend to the plot
ax.legend(loc='upper left', fontsize=10, frameon=False)

# Add grid lines for better readability
ax.grid(True, which='major', linestyle='--', alpha=0.7)

# Adjust x-axis ticks for clarity
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)

# Enhancing grid lines and adding minor ticks
ax.minorticks_on()
ax.grid(True, which='minor', linestyle=':', linewidth='0.5', alpha=0.5)

# Annotate specific years to highlight trends
important_years = [2015, 2020, 2023]
for i, year in enumerate(years):
    if year in important_years:
        total_usage = (traditional_mail[i] + email[i] + social_media[i] +
                       instant_messaging[i] + video_conferencing[i])
        ax.annotate(f"Total: {total_usage} units", (year, total_usage + 10),
                    textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color='black',
                    arrowprops=dict(arrowstyle='->', color='gray'))

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()