import numpy as np
import matplotlib.pyplot as plt

# Define the years and digital communication usage data (in arbitrary units)
years = np.arange(2010, 2021)

# Constructed data for each communication method (in arbitrary units)
email_usage = np.array([80, 78, 76, 75, 74, 73, 72, 70, 68, 66, 65])
social_media = np.array([10, 15, 25, 35, 45, 55, 70, 85, 95, 100, 105])
instant_messaging = np.array([5, 10, 15, 20, 30, 50, 65, 80, 100, 120, 130])
video_calls = np.array([2, 3, 5, 7, 10, 15, 20, 30, 50, 80, 110])

# Stacking the data
communication_data = np.vstack([email_usage, social_media, instant_messaging, video_calls])

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
stack = ax.stackplot(years, communication_data, labels=['Email', 'Social Media', 'Instant Messaging', 'Video Calls'],
                     colors=colors, alpha=0.8)

# Customize the plot
ax.set_title('Digital Communication Evolution (2010-2020)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Usage (Arbitrary Units)', fontsize=14)

# Add legend
ax.legend(loc='upper left', fontsize=12, title='Communication Method', frameon=False)

# Grid and minor grid lines
ax.grid(linestyle='--', alpha=0.6)
ax.minorticks_on()
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='gray', alpha=0.5)

# Enhance readability of x-axis labels
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 401, 50))

# Annotate significant points or changes
ax.annotate('Social Media Surge', xy=(2015, 160), xytext=(2013, 250),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='darkorange')

ax.annotate('Rise of Video Calls', xy=(2018, 200), xytext=(2016, 300),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='red'),
            fontsize=12, color='red')

# Add a description box
props = dict(boxstyle='round', facecolor='wheat', alpha=0.3)
textstr = ('The decade marked by shifting\n'
           'preferences in communication.\n'
           'Emergence of real-time, flexible,\n'
           'and interactive digital tools.')
ax.text(0.02, 0.97, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

# Automatically adjust the layout for better appearance
plt.tight_layout()

# Show the plot
plt.show()