import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the years from 2000 to 2020
years = np.arange(2000, 2021)

# Artificial data representing the perceived impact on language learning for each method
social_media_impact = np.array([3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9, 9, 8, 8, 9, 9, 10, 10, 9, 9, 10])
video_conferencing_impact = np.array([2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10])
online_forums_impact = np.array([5, 6, 6, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9])
instant_messaging_impact = np.array([4, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9])
traditional_writing_impact = np.array([8, 7, 7, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2])

# Set up the plot
plt.figure(figsize=(14, 8))

# Scatter plot for each communication method
plt.scatter(years, social_media_impact, color='blue', label='Social Media', s=50, zorder=3)
plt.scatter(years, video_conferencing_impact, color='green', label='Video Conferencing', s=50, zorder=3)
plt.scatter(years, online_forums_impact, color='red', label='Online Forums', s=50, zorder=3)
plt.scatter(years, instant_messaging_impact, color='purple', label='Instant Messaging', s=50, zorder=3)
plt.scatter(years, traditional_writing_impact, color='orange', label='Traditional Letter Writing', s=50, zorder=3)

# Create smooth fitting curves using spline interpolation
x_new = np.linspace(years.min(), years.max(), 300)
smooth_social_media = make_interp_spline(years, social_media_impact, k=3)(x_new)
smooth_video_conferencing = make_interp_spline(years, video_conferencing_impact, k=3)(x_new)
smooth_online_forums = make_interp_spline(years, online_forums_impact, k=3)(x_new)
smooth_instant_messaging = make_interp_spline(years, instant_messaging_impact, k=3)(x_new)
smooth_traditional_writing = make_interp_spline(years, traditional_writing_impact, k=3)(x_new)

# Plot the smooth fitting curves
plt.plot(x_new, smooth_social_media, color='blue', linestyle='-', alpha=0.5, zorder=2)
plt.plot(x_new, smooth_video_conferencing, color='green', linestyle='-', alpha=0.5, zorder=2)
plt.plot(x_new, smooth_online_forums, color='red', linestyle='-', alpha=0.5, zorder=2)
plt.plot(x_new, smooth_instant_messaging, color='purple', linestyle='-', alpha=0.5, zorder=2)
plt.plot(x_new, smooth_traditional_writing, color='orange', linestyle='-', alpha=0.5, zorder=2)

# Add title and labels
plt.title('Impact of Communication Methods on Language Learning\n(2000-2020)', fontsize=14, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Perceived Impact on Language Learning (Scale: 1 to 10)', fontsize=12)
plt.xticks(years, rotation=45)
plt.ylim(0, 11)
plt.grid(True, linestyle='--', alpha=0.5, zorder=1)

# Add legend
plt.legend(title='Communication Methods', loc='upper left', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()