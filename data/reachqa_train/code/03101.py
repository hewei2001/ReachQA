import matplotlib.pyplot as plt
import numpy as np

# Define the data for years
years = np.arange(1995, 2024)

# Data for each communication technology (in arbitrary units)
email_usage = np.array([
    10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
    58, 60, 63, 65, 68, 70, 72, 73, 74, 75,
    76, 77, 78, 78, 79, 80, 81, 81, 82
])

social_media_usage = np.array([
    0, 0, 0, 0, 0, 0, 5, 10, 15, 20,
    25, 30, 35, 40, 45, 50, 55, 58, 62, 65,
    68, 70, 73, 75, 78, 80, 82, 84, 86
])

video_conferencing_usage = np.array([
    0, 0, 0, 0, 0, 0, 0, 5, 7, 10,
    12, 15, 20, 25, 30, 35, 40, 45, 50, 55,
    60, 65, 70, 75, 80, 85, 88, 90, 92
])

messaging_apps_usage = np.array([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
    10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
    60, 65, 70, 75, 80, 85, 90, 95, 100
])

# Plotting setup
fig, ax = plt.subplots(figsize=(14, 8))

# Stacked area plot
ax.stackplot(years, email_usage, social_media_usage, video_conferencing_usage, messaging_apps_usage,
             labels=['Email', 'Social Media', 'Video Conferencing', 'Messaging Apps'],
             colors=['#FFD700', '#87CEEB', '#FF69B4', '#32CD32'], alpha=0.8)

# Customizing plot appearance
ax.set_title("Evolution of Digital Communication Technologies\nfrom 1995 to 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Global Usage (Arbitrary Units)', fontsize=14)
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 250)

# Set x-ticks to show every 5 years
ax.set_xticks(years[::5])

# Rotate x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Adding a legend
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Communication Mediums", fontsize=12)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the chart
plt.show()