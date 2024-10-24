import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2013, 2024)

# Internet traffic data in petabytes (hypothetical)
streaming_services = np.array([30, 40, 55, 65, 75, 90, 100, 115, 130, 150, 170])
online_gaming = np.array([15, 20, 22, 24, 28, 35, 45, 50, 58, 70, 85])
social_media = np.array([10, 12, 15, 20, 25, 35, 50, 60, 80, 100, 130])

# Calculate year-over-year growth rates (in percentage)
streaming_growth = np.round(np.diff(streaming_services) / streaming_services[:-1] * 100, 2)
online_gaming_growth = np.round(np.diff(online_gaming) / online_gaming[:-1] * 100, 2)
social_media_growth = np.round(np.diff(social_media) / social_media[:-1] * 100, 2)

# Creating the figure and the two subplots (1x2 layout)
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Plot the original line plot on the first subplot
ax1 = axes[0]
ax1.plot(years, streaming_services, marker='o', linestyle='-', color='#1f77b4', linewidth=2, label='Streaming Services')
ax1.plot(years, online_gaming, marker='s', linestyle='--', color='#ff7f0e', linewidth=2, label='Online Gaming')
ax1.plot(years, social_media, marker='^', linestyle='-.', color='#2ca02c', linewidth=2, label='Social Media')

# Customize the title and axis labels for the first plot
ax1.set_title('Internet Traffic Trends in FantasyLand\nA Decade of Digital Change', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Monthly Internet Traffic (Petabytes)', fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.legend(title='Digital Media Types', loc='upper left', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.6)

# Annotate key milestones
annotations = {
    2015: ("Mobile Streaming Surges", streaming_services[2]),
    2020: ("Gaming Goes Global", online_gaming[7]),
    2023: ("Social Media Dominance", social_media[10]),
}
for year, (text, y_value) in annotations.items():
    ax1.annotate(text, xy=(year, y_value), xytext=(year, y_value + 15),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5), fontsize=10, color='black', ha='center')

# Plot a bar chart for the growth rates on the second subplot
ax2 = axes[1]
bar_width = 0.25
years_growth = years[1:]  # Skip the first year since growth is calculated between years
x_indices = np.arange(len(years_growth))

ax2.bar(x_indices - bar_width, streaming_growth, width=bar_width, label='Streaming Services Growth', color='#1f77b4')
ax2.bar(x_indices, online_gaming_growth, width=bar_width, label='Online Gaming Growth', color='#ff7f0e')
ax2.bar(x_indices + bar_width, social_media_growth, width=bar_width, label='Social Media Growth', color='#2ca02c')

# Customize the second plot
ax2.set_title('Year-over-Year Growth Rates', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.set_xticks(x_indices)
ax2.set_xticklabels(years_growth, rotation=45)
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(axis='y', linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()