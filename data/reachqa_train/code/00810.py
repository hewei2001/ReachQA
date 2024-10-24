import numpy as np
import matplotlib.pyplot as plt

# Define the extended years
years = np.arange(2000, 2026)

# Constructed data for each communication method with more complexity
email_usage = np.array([90, 88, 87, 85, 84, 83, 82, 80, 78, 76, 75, 74, 73, 72, 70, 68, 66, 65, 63, 62, 60, 58, 55, 53, 50, 48])
social_media = np.array([5, 7, 10, 15, 25, 30, 35, 40, 45, 50, 55, 60, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135])
instant_messaging = np.array([2, 3, 5, 8, 12, 18, 24, 30, 40, 50, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 130, 135, 140])
video_calls = np.array([1, 1, 2, 3, 5, 7, 9, 12, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170])
text_messaging = np.array([50, 48, 46, 44, 42, 41, 40, 38, 37, 35, 33, 31, 29, 28, 27, 26, 25, 23, 22, 21, 20, 18, 17, 16, 15, 14])

# Constructing a realistic seasonal pattern for blogs with a sinusoidal approach
t = np.linspace(0, 2 * np.pi, years.size)
blogging = 5 + 4 * np.sin(t) + np.arange(years.size) * 0.5

# Stacking the data
communication_data = np.vstack([email_usage, social_media, instant_messaging, video_calls, text_messaging, blogging])

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(14, 10))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
ax.stackplot(years, communication_data, labels=[
    'Email', 'Social Media', 'Instant Messaging', 'Video Calls', 'Text Messaging', 'Blogging'],
    colors=colors, alpha=0.8)

# Customize the plot
ax.set_title('Digital Communication Evolution (2000-2025)\nAn Analysis of Trends Across Diverse Channels', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Usage (Arbitrary Units)', fontsize=14)

# Add legend
ax.legend(loc='upper left', fontsize=12, title='Communication Method', frameon=False)

# Enhance grid
ax.grid(linestyle='--', alpha=0.6)
ax.minorticks_on()
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='gray', alpha=0.5)

# Enhance readability of axis labels
plt.xticks(years[::2], rotation=45)
plt.yticks(np.arange(0, 401, 50))

# Annotate significant points or changes
ax.annotate('Social Media Surge', xy=(2015, 210), xytext=(2010, 320),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='darkorange'),
            fontsize=12, color='darkorange')

ax.annotate('Rise of Video Calls', xy=(2020, 250), xytext=(2015, 320),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='red'),
            fontsize=12, color='red')

# Add a description box
props = dict(boxstyle='round', facecolor='wheat', alpha=0.3)
textstr = ('The timeline showcases the dynamic\n'
           'shift in communication preferences,\n'
           'highlighting the growing impact of\n'
           'real-time and multimedia channels.')
ax.text(0.02, 0.97, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

# Automatically adjust the layout for better appearance
plt.tight_layout()

# Show the plot
plt.show()