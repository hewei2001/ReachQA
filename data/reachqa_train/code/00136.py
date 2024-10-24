import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Popularity index for each digital music format
mp3_popularity = [30, 40, 55, 70, 75, 80, 85, 88, 90, 87, 80, 78, 75, 70, 65, 60, 55, 50, 40, 35, 30]
aac_popularity = [10, 15, 25, 35, 45, 50, 55, 60, 65, 68, 70, 75, 78, 80, 85, 88, 90, 92, 93, 92, 90]
flac_popularity = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 88, 90, 92, 94]

# Plotting
plt.figure(figsize=(12, 8))

# Plot the popularity of each music format
plt.plot(years, mp3_popularity, marker='o', linestyle='-', linewidth=2, color='b', label='MP3')
plt.plot(years, aac_popularity, marker='s', linestyle='--', linewidth=2, color='g', label='AAC')
plt.plot(years, flac_popularity, marker='^', linestyle='-.', linewidth=2, color='r', label='FLAC')

# Fill area under the curves for a visual effect
plt.fill_between(years, mp3_popularity, color='b', alpha=0.1)
plt.fill_between(years, aac_popularity, color='g', alpha=0.1)
plt.fill_between(years, flac_popularity, color='r', alpha=0.1)

# Titles and labels
plt.title('The Evolution of Digital Music Formats:\nPopularity Over Time (2000-2020)', fontsize=14, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Popularity Index', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 101, 10))
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Legend
plt.legend(loc='upper right', fontsize=10, title='Music Format', title_fontsize='13')

# Annotations for peak popularity
plt.annotate('Peak MP3',
             xy=(2007, 90),
             xytext=(2003, 95),
             arrowprops=dict(facecolor='blue', shrink=0.05),
             fontsize=10, color='blue')
plt.annotate('Peak AAC',
             xy=(2020, 90),
             xytext=(2015, 95),
             arrowprops=dict(facecolor='green', shrink=0.05),
             fontsize=10, color='green')
plt.annotate('Peak FLAC',
             xy=(2020, 94),
             xytext=(2016, 98),
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=10, color='red')

# Layout adjustment
plt.tight_layout()

# Display the chart
plt.show()