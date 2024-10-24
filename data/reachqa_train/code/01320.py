import matplotlib.pyplot as plt
import numpy as np

# Define the years for which data is available
years = np.arange(2010, 2021)

# Define the streaming platforms
platforms = ["Streaming A", "Streaming B", "Streaming C", "Streaming D", "Other Platforms"]

# Hours of content streamed globally (in billion hours) for each platform
streamed_hours = np.array([
    [10, 15, 20, 25, 32, 40, 55, 68, 75, 80, 82],  # Streaming A
    [5, 10, 15, 20, 28, 35, 45, 50, 55, 60, 65],   # Streaming B
    [2, 5, 9, 14, 20, 28, 38, 45, 50, 55, 60],     # Streaming C
    [1, 2, 5, 10, 15, 20, 28, 30, 32, 34, 36],     # Streaming D
    [5, 6, 8, 11, 15, 20, 25, 30, 32, 35, 37]      # Other Platforms
])

# Calculate the year-over-year growth rates
growth_rates = np.diff(streamed_hours) / streamed_hours[:, :-1] * 100

# Set up the figure and subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 8))
fig.suptitle('The Rise of Streaming:\nEvolution of Digital Streaming Platforms from 2010 to 2020', fontsize=16, fontweight='bold', y=1.02)

# Colors for plotting
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot the stacked area chart
axes[0].stackplot(years, streamed_hours, labels=platforms, colors=colors, alpha=0.85)
axes[0].set_title('Overall Streaming Growth', fontsize=14)
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Hours Streamed (in billion hours)', fontsize=12)
axes[0].legend(loc='upper left', fontsize=10, title='Streaming Platforms', bbox_to_anchor=(1, 1))
axes[0].yaxis.grid(True, linestyle='--', alpha=0.7)
axes[0].set_xticks(years)
axes[0].tick_params(axis='x', rotation=45)

# Plot the line chart for year-over-year growth rates
for i, platform in enumerate(platforms):
    axes[1].plot(years[1:], growth_rates[i], label=platform, color=colors[i], marker='o')

axes[1].set_title('Year-over-Year Growth Rates by Platform', fontsize=14)
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Growth Rate (%)', fontsize=12)
axes[1].legend(loc='upper left', fontsize=10, title='Streaming Platforms', bbox_to_anchor=(1, 1))
axes[1].axhline(0, color='grey', linewidth=0.8, linestyle='--')
axes[1].yaxis.grid(True, linestyle='--', alpha=0.7)
axes[1].set_xticks(years[1:])
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout(pad=3)
plt.show()