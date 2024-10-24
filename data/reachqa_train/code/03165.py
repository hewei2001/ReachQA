import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2013, 2024)

# Artificial data for digital media consumption (in millions) per year for each category
video_streaming = [50, 65, 80, 95, 115, 135, 160, 190, 220, 250, 280]
music_streaming = [30, 35, 40, 50, 60, 75, 95, 115, 135, 160, 180]
podcasts = [5, 8, 12, 18, 25, 33, 43, 55, 70, 85, 100]
ebooks = [10, 12, 15, 18, 22, 28, 35, 42, 50, 60, 70]

# Combine datasets for the stackplot
media_types = np.array([video_streaming, music_streaming, podcasts, ebooks])

# Calculate the growth rate for each category
growth_rates = [np.diff(category) / category[:-1] * 100 for category in media_types]

# Create the plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7), gridspec_kw={'width_ratios': [2, 1]})

# Plot stackplot on the first subplot
ax1.stackplot(years, media_types, labels=['Video Streaming', 'Music Streaming', 'Podcasts', 'E-books'],
              colors=['skyblue', 'limegreen', 'coral', 'purple'], alpha=0.8)

ax1.set_title("Evolution of Digital Media Consumption in TechTropolis\n(2013-2023)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Consumption (Millions of Users)", fontsize=12)
ax1.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Media Type', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.tick_params(axis='x', rotation=45)

# Plot line chart on the second subplot
for growth_rate, label, color in zip(growth_rates, ['Video Streaming', 'Music Streaming', 'Podcasts', 'E-books'],
                                     ['skyblue', 'limegreen', 'coral', 'purple']):
    ax2.plot(years[1:], growth_rate, label=label, color=color, marker='o')

ax2.set_title("Annual Growth Rate of Digital Media Consumption", fontsize=14, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Growth Rate (%)", fontsize=12)
ax2.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Media Type', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.tick_params(axis='x', rotation=45)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()