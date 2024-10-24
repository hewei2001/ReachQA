import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Define the years for the x-axis
years = np.arange(2000, 2021)

# Simulated adoption data for communication methods (in arbitrary units)
email_adoption = np.array([50, 55, 60, 65, 70, 75, 80, 85, 88, 90, 92, 93, 94, 95, 96, 97, 98, 99, 99, 99, 100])
instant_messaging = np.array([5, 10, 15, 20, 30, 40, 55, 60, 65, 70, 75, 80, 82, 85, 87, 89, 90, 92, 93, 95, 97])
video_calls = np.array([1, 2, 3, 4, 5, 8, 12, 18, 25, 35, 45, 55, 60, 68, 75, 82, 88, 92, 95, 97, 99])
social_media = np.array([2, 3, 5, 8, 12, 20, 30, 45, 60, 75, 85, 90, 92, 94, 95, 97, 98, 99, 100, 100, 100])
phone_calls = np.array([95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 3, 2])

# Create a stacked area chart with a harmonious color palette
fig, ax = plt.subplots(figsize=(14, 9))

colors = ['#FFB6C1', '#87CEEB', '#98FB98', '#FFD700', '#D2691E']
ax.stackplot(years, email_adoption, instant_messaging, video_calls, social_media, phone_calls,
             labels=['Email', 'Instant Messaging', 'Video Calls', 'Social Media', 'Phone Calls'],
             colors=colors, alpha=0.85)

# Add trend lines for clarity with borders to enhance distinction
borders = ['#FF69B4', '#4682B4', '#228B22', '#FFA500', '#8B0000']
for adoption, border in zip([email_adoption, instant_messaging, video_calls, social_media, phone_calls], borders):
    ax.plot(years, adoption, color=border, linestyle='--', linewidth=1)

# Add annotations for significant events
ax.annotate('Rise of Social Media', xy=(2010, social_media[10]), xytext=(2005, 85),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='white')
ax.annotate('Smartphone Boom', xy=(2012, instant_messaging[12]), xytext=(2007, 65),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='white')

# Title and labels
ax.set_title("The Digital Evolution in Communication Methods\n(2000-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Adoption Rate (Arbitrary Units)", fontsize=12)

# Customize grid style
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Set ticks for both axes
ax.set_xticks(years[::2])
ax.set_yticks(np.arange(0, 101, 10))

# Rotate x-tick labels for better readability
ax.set_xticklabels(years[::2], rotation=45, ha='right')

# Add a legend with icons
legend_elements = [Patch(facecolor=colors[i], edgecolor=borders[i], label=label)
                   for i, label in enumerate(['Email', 'Instant Messaging', 'Video Calls', 'Social Media', 'Phone Calls'])]
ax.legend(handles=legend_elements, loc='upper left', fontsize=10, bbox_to_anchor=(1, 1), title="Communication Methods")

# Highlight recent years
ax.axvspan(2018, 2020, color='lightgray', alpha=0.3)

# Adjust layout to prevent overlapping text
plt.tight_layout()

# Display the plot
plt.show()