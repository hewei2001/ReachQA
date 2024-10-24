import matplotlib.pyplot as plt
import numpy as np

# Define the years for the data
years = np.array([2020, 2021, 2022, 2023, 2024])

# Daily Active Users (in millions) for each platform over the years
chatbuzz_daus = np.array([5, 8, 12, 20, 27])
picsharper_daus = np.array([4, 7, 9, 13, 16])
storystream_daus = np.array([2, 4, 7, 11, 18])
snapcast_daus = np.array([6, 9, 13, 18, 23])
musicwave_daus = np.array([3, 6, 8, 12, 15])

# Create the line chart
fig, ax = plt.subplots(figsize=(12, 6))

# Plot each platform's DAUs over the years
ax.plot(years, chatbuzz_daus, label='ChatBuzz', color='navy', linewidth=2, marker='o')
ax.plot(years, picsharper_daus, label='PicSharper', color='firebrick', linewidth=2, marker='s')
ax.plot(years, storystream_daus, label='StoryStream', color='forestgreen', linewidth=2, marker='^')
ax.plot(years, snapcast_daus, label='SnapCast', color='darkorange', linewidth=2, marker='D')
ax.plot(years, musicwave_daus, label='MusicWave', color='purple', linewidth=2, marker='*')

# Set titles and labels
ax.set_title("Tech Trends: Growth in Daily Active Users\nEmerging Social Media Platforms (2020-2024)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Daily Active Users (in millions)", fontsize=12)

# Add a legend
ax.legend(loc='upper left', fontsize=10, frameon=False)

# Enable grid for better readability
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Set the limits for the axes
ax.set_xlim(min(years), max(years))
ax.set_ylim(0, 30)

# Add annotations for specific observations
ax.annotate('Rapid Expansion', xy=(2024, 27), xytext=(2022.5, 29),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, ha='center', fontstyle='italic', color='navy')

# Show data values on each point
for year, cb, ps, ss, sc, mw in zip(years, chatbuzz_daus, picsharper_daus, storystream_daus, snapcast_daus, musicwave_daus):
    ax.text(year, cb + 0.5, f'{cb}', fontsize=9, ha='center', color='navy')
    ax.text(year, ps + 0.5, f'{ps}', fontsize=9, ha='center', color='firebrick')
    ax.text(year, ss + 0.5, f'{ss}', fontsize=9, ha='center', color='forestgreen')
    ax.text(year, sc + 0.5, f'{sc}', fontsize=9, ha='center', color='darkorange')
    ax.text(year, mw + 0.5, f'{mw}', fontsize=9, ha='center', color='purple')

# Adjust layout to prevent clipping of text and overlapping
plt.tight_layout()

# Display the chart
plt.show()